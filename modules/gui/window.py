import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self.SIZE = 0.8
        self.WIDTH = int(self.winfo_screenwidth() * self.SIZE)
        self.HEIGHT = int(self.winfo_screenheight() * self.SIZE)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.title("Edit Image")

app = App()