# Prokudin_Gorsky
Programm that takes as input a scan of Prokudin-Gorsky film with three separate color channels of a photograph, and returns a color image obtained by combining the channels.
Example:
INPUT
![1](https://user-images.githubusercontent.com/33635536/179764078-bbdd23c3-0a32-4898-a3d4-6ccc4a646280.jpg)
OUTPUT
![2](https://user-images.githubusercontent.com/33635536/179764127-dbe237d9-9463-43b3-9cdd-31ca4ce5a464.jpg)

This program could be run without any parameters, you only have to put your input image named "pic.jpg" in the same folder as py-file.
Also you can run it from command line giving path to image as a parameter (example: "main.py input_image.tif")

The function takes the following parameters:
picname - input file name (default "pic.jpg")
cut_percent - the percentage of the image that will be cut off from both sides of the input image (default 0.1)
out_name - output file name (default "result.jpg")
logs - show information about alignment progress in the console (default is False)
show_result - display the result in a separate window when finished (default is False)
