import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import random
import io   

# Monka
def fetch_random_monkey():
    response = requests.get("https://source.unsplash.com/random?monkey")
    image_bytes = io.BytesIO(response.content)
    monkey_image = Image.open(image_bytes)
    return monkey_image

def generate_monkey():
    monkey_image = fetch_random_monkey()

    # Resize
    window_width, window_height = root.winfo_width(), root.winfo_height()
    monkey_image.thumbnail((window_width, window_height))

    photo = ImageTk.PhotoImage(monkey_image)
    image_label.config(image=photo)
    image_label.image = photo

# QuitBox
def on_closing():
    if messagebox.askyesno("Quit", "Do you want to quit?"):
        if messagebox.askyesno("Confirm", "Do you really want to?"):
            messagebox.showinfo("Goodbye", "uUU aAA AaaA uh uh wuogh")
            root.destroy()

# Main Window
root = tk.Tk()
root.title("Random Monkey Generator")

# Window Size
window_width, window_height = 400, 300
root.geometry(f"{window_width}x{window_height}")

# Button
generate_button = tk.Button(root, text="Generate Monkey", command=generate_monkey)
generate_button.pack()

# Display Monka
image_label = tk.Label(root)
image_label.pack()

# Window Closing
root.protocol("WM_DELETE_WINDOW", on_closing)

# Loop
root.mainloop()
