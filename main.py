"""
Project: PPM image viewer
Author: Ricardo Santinho Horta
Date: 08/12/2025
Description: Converts P6 images to P3 and displays them in Tkinter.
"""

from PIL import Image, ImageTk
import tkinter as tk
import converter
root = tk.Tk()


def file_to_image(input_path):
    """
    Displays the ppm file in a tkinter window.

    :param input_path: ppm image path.
    :return: a tkinter window with the corresponding to the ppm file.
    """
    file = input_image_ver(input_path)
    with open(file, "r") as f:
        print("\nmain - def file_to_image\nf Name in: " + f.name + " | Mode: " + f.mode)
        magic = f.readline().strip()
        width, height = map(int, f.readline().split())
        maxval = int(f.readline().strip())

        data = []
        for line in f:
            data.extend(map(int, line.split()))

        pixels = [tuple(data[i:i+3]) for i in range(0, len(data), 3)]

    img = Image.new("RGB", (width, height))
    j = 0
    for y in range(height):
        for x in range(width):
            img.putpixel((x, y), pixels[j])
            j += 1

    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_img)
    label.image = tk_img
    label.pack()


def input_image_ver(input_path):
    """
    Check if the provided file is in ppm3, ppm6, or another format.

    :param input_path: ppm image path.
    :return: If it's either mpp3 or mpp6, it returns the image path; otherwise, it returns an error.
    """
    with open(input_path, 'rb') as f:
        print("\nmain - def input_image_ver\nf Name in: " + f.name + " | Mode: " + f.mode)

        img_first_line = f.readline().strip()
        
        if img_first_line == b"P6":
            converter.converter(input_path)
            return "output.ppm"
        
        elif img_first_line == b"P3":
            return input_path
        
        else:
            print("\nfrom main.input_image_ver: Error: f must be in ppm P6 format.\n")
            return sys.exit(1)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Use: py main.py <image.ppm>")
        sys.exit(1)

    path = sys.argv[1]
    file_to_image(path)


    root.mainloop()
