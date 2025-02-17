from tkinter import filedialog
from ..gui.button import ButtonApp
import customtkinter as ctk
from ..gui.image import ImageApp

list_image = []
def show_image(image_app: ImageApp):
    # Беремо кожну картинку та приховуємо її
    for image in list_image:
        # pack_forget - приховуємо картинку
        image.pack_forget()
    # Відображаємо картинку
    image_app.pack()

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

        image_app = ImageApp(
            image_path = path,
            master_ch = image_master
        )
        list_image.append(image_app)
        button = ButtonApp(
            master = button_master,
            height = 30,
            width = button_master._current_width * 0.8,
            text = name,
            command = lambda image = image_app: show_image(image)
        )
        button.pack(pady = 10)