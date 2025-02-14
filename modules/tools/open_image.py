from tkinter import filedialog
from ..gui.button import ButtonApp
import customtkinter as ctk
from ..gui.image import ImageApp

def open_file(button_master: ctk.CTkFrame | ctk.CTkScrollableFrame, parent: ctk.CTk, image_master: ctk.CTkFrame):
    file_paths = filedialog.askopenfilenames(
        filetypes = [("Images", ["*.png", "*.jpg", "*.ico", "*.svg", "*.jpeg"])],
        initialdir= "/",
        title = "Choose images",
        parent = parent
    )
    for path in file_paths:
        print(f'Select image: {path}')
        name = path.split("/")[-1]
        button = ButtonApp(
            master = button_master,
            height = 30,
            width = button_master._current_width * 0.8,
            text = name
        )
        button.pack(pady = 10)
        
        image = ImageApp(
            image_path = path,
            master_ch = image_master
        )
        image.pack()