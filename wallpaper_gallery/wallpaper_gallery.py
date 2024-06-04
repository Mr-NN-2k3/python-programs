from tkinter import *
from PIL import Image, ImageTk
import os

# Global counter to keep track of the current image index
counter = 0

# Function to display the next image in the list


def next_image():
    global counter
    counter += 1
    img_display.config(image=img_list[counter])

# Function to display the previous image in the list


def previous_image():
    global counter
    counter -= 1
    img_display.config(image=img_list[counter])


# Create the main Tkinter window
root = Tk()

# Set window title and background color
root.title("Wallpaper gallery")
root.config(bg="black")

# Maximize the window
root.state("zoomed")

# Directory containing the images
imgs_dir = "wallpaper_gallery/wallpapers"

# List all files in the directory
wallpapers = os.listdir(imgs_dir)

# List to store PhotoImage objects for the images
img_list = []

# Load each image, resize it, and create a PhotoImage object
for files in wallpapers:
    try:
        img = Image.open(os.path.join(imgs_dir, files))
        resized = img.resize((1080, 720))
        img_list.append(ImageTk.PhotoImage(resized))
        img.close()
    except Image.DecompressionBombWarning as e:
        print(f"Warning: {e}")
    except Exception as e:
        print(f"Error loading image {files}: {e}")

# Check if any images were loaded successfully
if img_list:
    # Display the first image
    img_display = Label(root, image=img_list[0])
    img_display.pack(pady=(20, 20))
    img_display.config(bg="black")
else:
    print("No images loaded.")

# Create a frame to hold the navigation buttons
button_frame = Frame(root, bg="black")
button_frame.pack(side="top", pady=(20))

# Create the Next button
next_btn = Button(button_frame, text="Next",
                  command=next_image, width=20, height=2)
next_btn.pack(side="left", padx=10)

# Create the Previous button
previous_btn = Button(button_frame, text="Previous",
                      command=previous_image, width=20, height=2)
previous_btn.pack(side="left", padx=10)

# Start the Tkinter event loop
root.mainloop()
