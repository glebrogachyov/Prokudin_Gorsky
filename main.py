from skimage.io import imread, imshow, imsave
from skimage import img_as_float, img_as_ubyte
from skimage.transform import rescale
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
from datetime import datetime
from sys import argv
import numpy as np
import os


def time_info_dec(full_info: bool = False):
    def time_dec(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            if full_info:
                print(f"----\nStarted:\t\t\t {start_time}\n----")
            res = func(*args, **kwargs)
            end_time = datetime.now()
            if full_info:
                print(f"\n----\nEnded:\t\t\t\t {end_time}")
            time_diff = end_time - start_time
            print(f"\nExecution time:\t\t {time_diff}\n----")
            return res
        return wrapper
    return time_dec


def count_shift(r, g, b):
    shift_range = 3
    ch_shift = np.array([[0, 0], [0, 0]])
    for ch, shift in [(r, ch_shift[0]), (b, ch_shift[1])]:
        corr = 0
        for ver in range(-shift_range, shift_range+1):
            tmpp = np.roll(ch, ver, 0)
            for hor in range(-shift_range, shift_range+1):
                tmp = np.roll(tmpp, hor, 1)
                correlation = (g * tmp).sum()
                if correlation > corr:
                    corr = correlation
                    shift[0], shift[1] = ver, hor
    return ch_shift


def align(r, g, b, res, logs=False, calls=0):
    if r.shape[1] > 125:
        calls += 1
        if logs:
            print("\t" * (calls - 1), "Scale 1:", 2 ** (calls - 1), sep='')
        ch_shift = align(rescale(r, 0.5), rescale(g, 0.5), rescale(b, 0.5), res, logs, calls)
        res += ch_shift
        res *= 2
        r = np.roll(r, res[0][0], axis=0)
        r = np.roll(r, res[0][1], axis=1)
        b = np.roll(b, res[1][0], axis=0)
        b = np.roll(b, res[1][1], axis=1)
        if logs:
            print("\t" * (calls-1), "Shifting 1:", 2 ** (calls - 1), sep='')
    return count_shift(r, g, b)


@time_info_dec(True)
def main(picname, cut_percent=0.1, out_name="result.jpg", logs=False, show_result=False):
    if logs:
        print("Reading image ...")
    img = img_as_float(imread(picname))
    if len(img.shape) > 2:
        print("Number of channels > 1. Reshaping to 1")
        img = rgb2gray(img)
    if logs:
        print("Processing...")
    h, w = img.shape[0], img.shape[1]
    part = h // 3
    b, g, r = img[0:part], img[part:2 * part], img[2 * part:3 * part]
    h, w = int(part * cut_percent), int(w * cut_percent)
    r = np.array(r[h: -h, w: -w])
    g = np.array(g[h: -h, w: -w])
    b = np.array(b[h: -h, w: -w])
    ch_shift = np.array([[0, 0], [0, 0]])
    ch_shift += align(r, g, b, ch_shift, logs)
    if logs:
        print("Creating output image...")
    r = np.roll(r, ch_shift[0][0], axis=0)
    r = np.roll(r, ch_shift[0][1], axis=1)
    b = np.roll(b, ch_shift[1][0], axis=0)
    b = np.roll(b, ch_shift[1][1], axis=1)
    result = np.dstack((r, g, b))
    if show_result:
        imshow(result)
        plt.show()
    if logs:
        print("Done.")
    result = img_as_ubyte(result)
    imsave(out_name, result)
    return 1



if __name__ == "__main__":
    params = argv[1:]
    filename = params[0] if len(params) else 'pic.jpg'
    if filename in os.listdir():
        main(filename, cut_percent=0.075, out_name="res.jpg", logs=True, show_result=False)
    else:
        print("No file named '{}' in directory. Exit.".format(filename))
        exit(1)
