from tkinter import filedialog


def open_file():
    file_paths = filedialog.askopenfilenames(
        filetypes = [("Images", ["*.png", "*.jpg", "*.ico", "*.svg", "*.jpeg"])],
        initialdir= "/",
        title = "Choose images"
    )
    for path in file_paths:
        print(f'Select image: {path}')
        name = path.split("/")[-1]
        print(name)