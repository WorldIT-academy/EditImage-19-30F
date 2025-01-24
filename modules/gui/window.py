import customtkinter as ctk
from .frame_configuration import FrameApp

class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self, fg_color="#FFF")
        
        self.SIZE = 0.7
        
        self.WIDTH = int(self.winfo_screenwidth() * self.SIZE)
        self.HEIGHT = int(self.winfo_screenheight() * self.SIZE)
        
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.title("Edit Image")
        
        header_height = int(self.HEIGHT * 0.0585)
        self.HEADER = FrameApp(
            master_child = self,
            width_child = self.WIDTH,
            height_child = header_height,
            bg_color_child = "#373535",
        )
        
        self.HEADER.place(x = 0, y = 0)
        
        self.CONTENT = FrameApp(
            master_child = self,
            width_child = self.WIDTH,
            height_child = self.HEIGHT - header_height - 1,
            bg_color_child = "#1F1F1F"
        )    
        self.CONTENT.place(x = 0, y = header_height + 1)

app = App()