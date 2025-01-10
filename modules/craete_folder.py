from os.path import abspath, join
import os

def create_media_folder():
    path = abspath(join(__file__ , '..', '..', 'media')) 
    os.makedirs(name = join(path, "images", "downloads"), exist_ok= True  )    
    print(path)
create_media_folder()