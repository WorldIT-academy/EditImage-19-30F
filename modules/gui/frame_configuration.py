r"""
    ### У цьому файлі створюється інструкція (клас FrameApp), яка допомогає створювати вікна у додатку

    Приклад використання:
    
    ```python
        self.CONTENT = FrameApp(
            master_child = self,
            width_child = self.WIDTH,
            height_child = self.HEIGHT - header_height - 1,
            bg_color_child = "#1F1F1F"
        )  
    ```
    r перед многострочным комментарием игнорирует специальные символы ( \n ) в тексте
    [Посилання на github файлу](https://github.com/WorldIT-academy/EditImage-19-30F/blob/master/modules/gui/frame_configuration.py)
"""
import customtkinter as ctk

class FrameApp(ctk.CTkFrame):
    r"""
    ### Інструкція (клас), що допомогає створювати та налаштовувати вікна в додатку

    #### Параметри класу FrameApp:
        - `master_child` - батьківський елемент, до якого потрібно додати вікно
        - `width_child` - ширина створюванного елементу
        - `height_child` - висота створюванного елементу
        - `bg_color_child` - колір фону створюванного елементу
    """
    def __init__(self, master_child: object, width_child: int, height_child: int, bg_color_child: str):
        r"""
        ### Інструкція (клас), що допомогає створювати та налаштовувати вікна в додатку

        #### Параметри класу FrameApp:
            - `master_child` - батьківський елемент, до якого потрібно додати вікно
            - `width_child` - ширина створюванного елементу
            - `height_child` - висота створюванного елементу
            - `bg_color_child` - колір фону створюванного елементу
        """
        ctk.CTkFrame.__init__(
            self = self,
            master = master_child,
            width = width_child,
            height = height_child,
            fg_color= bg_color_child,
            corner_radius=0
        )