import PIL.Image
import customtkinter as ctk
from ..tools.create_folder import RED, YELLOW, RESET_ALL, GREEN
import PIL

class ImageApp(ctk.CTkLabel): 
    def __init__(self, master_ch: ctk.CTkFrame, image_path: str):
        self.IMAGE_PATH = image_path
        self.WIDTH = master_ch._current_width * 0.9
        self.HEIGHT = master_ch._current_height * 0.9
        ctk.CTkLabel.__init__(
            self = self,
            master = master_ch,
            text = "",
            image = self.load_image()
        )
    def load_image(self):
        try: 
            image = PIL.Image.open(self.IMAGE_PATH)
            return ctk.CTkImage(
                light_image = image,
                size = (self.WIDTH, self.HEIGHT)
            )
        except Exception as error:
            print(f"{RED}Error image load: {YELLOW}{error}{RESET_ALL}")