import PIL.Image
import customtkinter as ctk
from ..tools.create_folder import RED, YELLOW, RESET_ALL, GREEN

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
            size = self.image_size(image)
            print(size)
            return ctk.CTkImage(
                light_image = image,
                size = size
            )
        except Exception as error:
            print(f"{RED}Error image load: {YELLOW}{error}{RESET_ALL}")
    def image_size(self, image_s: PIL.Image):
        # Якщо, зображення квадратне
        if image_s.width == image_s.height:
            return (self.HEIGHT, self.HEIGHT)
        # Якщо, зображення НЕ квадратне
        else:
            # Якщо, ширина бiльша
            if image_s.width > self.WIDTH:
                # Пiдлаштовуємо висоту пiд ширину
                return (self.WIDTH, image_s.height / (image_s.width / self.WIDTH))
            # Якщо висота бiльша
            if image_s.height > self.WIDTH:
                # Пiдлаштовуємо ширину пiд висоту
                return (image_s.width / (image_s.height / self.HEIGHT), self.HEIGHT)
            
            # Якщо зображення менше
            return (image_s.width, image_s.height)
        