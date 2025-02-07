import customtkinter as ctk
import os
import PIL.Image
from ..create_folder import RED , RESET_ALL, YELLOW

class ButtonApp(ctk.CTkButton):
    def __init__(self, master: object, width: int, height: int, name_image: str, command = None, text = None,**kwargs):
        self.NAME_IMAGE = name_image
        self.SIZE = (width, height)
        
        ctk.CTkButton.__init__(
            self = self,
            master = master,
            width= width,
            height= height, 
            image = self.load_image(),
            command = command, 
            text = text,  
            corner_radius = 10,
            fg_color = master._fg_color,
            hover_color = "#373535",
            **kwargs
        )
    def load_image(self):
        path = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'static', 'icons', self.NAME_IMAGE))
        try:    
            image = PIL.Image.open(path)
            return ctk.CTkImage(
                light_image = image,
                size = self.SIZE
            )
        except Exception as error:
            print(f'{RED}Error load image: {YELLOW}{error}{RESET_ALL}')