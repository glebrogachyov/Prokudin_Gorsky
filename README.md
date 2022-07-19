# Prokudin_Gorsky
Programm that takes as input a scan of Prokudin-Gorsky film with three separate color channels of a photograph, and returns a color image obtained by combining the channels.
The program first halves the original image several times, then calculates the optimal shift on a small image, and then refines it for larger images. In contrast to the standard alignment algorithm, in which the channels of the original image are shifted relative to each other in a large range, this approach can greatly reduce the computation time for large images without losing quality.
- This program could be run without any parameters, you only have to put your input image named "pic.jpg" in the same folder as py-file.
- Also you can run it from command line giving path to image as a parameter (example: "main.py input_image.tif")

Example:

![ex2](https://user-images.githubusercontent.com/33635536/179773778-81e6be83-a503-4f8e-b8b9-0b7b9fcd61d4.jpg)





## The function takes the following parameters:

+ picname - input file name (default "pic.jpg")
+ cut_percent - the percentage of the image that will be cut off from both sides of the input image (default 0.1)
+ out_name - output file name (default "result.jpg")
+ logs - show information about alignment progress in the console (default is False)
+ show_result - display the result in a separate window when finished (default is False)
