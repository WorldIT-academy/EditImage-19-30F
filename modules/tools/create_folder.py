"""
Файл який створює функцiю create_media_folder
"""
from os.path import abspath, join, exists
import os
import colorama

GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
RED = colorama.Fore.RED
# colorama.Style.RESET_ALL - відміняє усі стилі
RESET_ALL = colorama.Style.RESET_ALL
# функція яка створює папку media
# """ текст """ - багаторядковий коментар, потрiбен для опису файлiв, функцiй та класiв. Та звичайного коментування 
def create_media_folder():
    """
    Функція яка створює папки downloads та edits у папці media
    """
    # try - намагається виконати код
    # except - якщо у try виникла помилка код переходить до except
    """
    try:
        Код який може мiстити помилку
    except Exception as error:
        Код в разi виникнення помилки
    """
    try:
        # отримуємо абсолютний шлях до папки media
        # abspath - збирає (будує) абсолютний шлях 
        # join - об'єднує частини шляху
        # __file__ - змінна, яка зберігає шлях до поточного файлу
        # '..' - частина шляху, яка повертає на папку назад
        path = abspath(join(__file__, '..', '..', '..', 'media'))
        # makedirs - створює папки з їх внутрішніми папками ( вкладенi папки )
        # exist_ok - запобігає помилку, якщо папка вже існує
        for folder_name in ["downloads", "edits"]:
            folder_path = join(path, "images", folder_name)
            # not - логiчний оператор який виконує умову якщо вона не дiйсна 
            if not exists(folder_path):
                print(f"{GREEN}Creating folder - {YELLOW}images/{folder_name}{RESET_ALL}")
                
            os.makedirs(name = folder_path, exist_ok=True)
    except Exception as error:
        print(f'{RED}Error: {error}{RESET_ALL}')

create_media_folder()