# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2

import tkinter as tk
from tkinter import filedialog
def apply_grayscale_filter(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def show_img():
    # Read the file
    image_path = 'sample.jpeg'
    image = cv2.imread(image_path)

    # Display the image in a window
    cv2.imshow('Image', image)

    # Apply grayscale filter
    grayscale_image=apply_grayscale_filter(image)

    # Display the grayscale image in a window
    cv2.imshow("Grayscale Image",grayscale_image)

    # Wait until a key is pressed and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def show_img2():
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select an image file from file explorer using the file dialog
    image_path = filedialog.askopenfilename(title="Select an image file",
                                            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    if image_path == "":
        print("Error: unable to load image")
        return

    # Read the file
    image = cv2.imread(image_path)

    # Display the image in a window
    cv2.imshow('Image', image)

    # Apply grayscale filter
    grayscale_image=apply_grayscale_filter(image)

    # Display the grayscale image in a window
    cv2.imshow("Grayscale Image",grayscale_image)

    # Wait until a key is pressed and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    #show_img()
    show_img2()
