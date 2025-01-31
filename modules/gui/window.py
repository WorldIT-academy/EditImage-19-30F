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
        self.resizable(False, False)
        
        header_height = int(self.HEIGHT * 0.0585)
        self.HEADER = FrameApp(
            master_child = self,
            width_child = self.WIDTH,
            height_child = header_height,
            bg_color_child = "#1F1F1F",
        )
        
        self.HEADER.place(x = 0, y = 0)
        
        self.CONTENT = FrameApp(
            master_child = self,
            width_child = self.WIDTH,
            height_child = self.HEIGHT - header_height - 1,
            bg_color_child = "#FFF"
        )    
        self.CONTENT.place(x = 0, y = header_height + 1)
        
        self.VERTICAL_MENU = FrameApp(
            master_child = self.CONTENT,
            width_child= self.WIDTH * 0.055,
            height_child= self.HEIGHT - header_height - 1,
            bg_color_child = "#1F1F1F"
        )
        self.VERTICAL_MENU.place(x = 0, y = 0)

        self.EXPLORER = FrameApp(
            master_child = self.CONTENT,
            width_child= self.WIDTH * 0.15,
            height_child= self.HEIGHT - header_height - 1,
            bg_color_child = "#1F1F1F"
        )
        self.EXPLORER.place(x = self.WIDTH * 0.055, y = 0)
        x_image = self.WIDTH * 0.15 + self.WIDTH * 0.055 
        self.SHOW_IMAGE = FrameApp(
            master_child = self.CONTENT,
            width_child = self.WIDTH - x_image,
            height_child = self.HEIGHT - header_height - 1,
            bg_color_child = "#FFF"
        )
        self.SHOW_IMAGE.place (x = x_image + 1 , y = 0)
        
        self.HEADER_SHOW_IMAGE  = FrameApp(
            master_child= self.SHOW_IMAGE,
            width_child = self.WIDTH - x_image,
            height_child = self.HEIGHT * 0.0391,
            bg_color_child = "#1F1F1F"
        )
        
        self.HEADER_SHOW_IMAGE.place(x = 0 , y = 0)
        
        self.IMAGE_BLOCK = FrameApp(
            master_child= self.SHOW_IMAGE,
            width_child = self.WIDTH - x_image,
            height_child= self.HEIGHT * 0.9609,
            bg_color_child= "#1F1F1F"
        )
        
        self.IMAGE_BLOCK.place(x = 0, y = self.HEIGHT * 0.0391)
app = App()