from tkinter import filedialog
from ..gui.button import ButtonApp
import customtkinter as ctk

def open_file(button_master: ctk.CTkFrame | ctk.CTkScrollableFrame):
    file_paths = filedialog.askopenfilenames(
        filetypes = [("Images", ["*.png", "*.jpg", "*.ico", "*.svg", "*.jpeg"])],
        initialdir= "/",
        title = "Choose images"
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