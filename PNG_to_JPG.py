# This function converts a PNG file into a JPG file 
import os 
from  PIL import Image 



def convert_rgba(fpath1):
    rgba_image = Image.open(fpath1)
    rgba_image.load()
    background = Image.new("RGB", rgba_image.size, (255, 255, 255))
    background.paste(rgba_image, mask = rgba_image.split()[3])
    JPG_fpath = rename_to_jpg(fpath1)
    print(f"removing file - {fpath1}")
    background.save(JPG_fpath, "JPEG", quality=100)
    print(f"Creating - {JPG_fpath}")
#     os.remove(fpath1)#remove the PNG file permanently
    
