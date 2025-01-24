import customtkinter as ctk

class FrameApp(ctk.CTkFrame):
    def __init__(self, master_child: object, width_child: int, height_child: int, bg_color_child: str):
        ctk.CTkFrame.__init__(
            self = self,
            master = master_child,
            width = width_child,
            height = height_child,
            fg_color= bg_color_child,
            corner_radius=0
        )