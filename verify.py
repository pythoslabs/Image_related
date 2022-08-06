# Created : 2 Jan 2022 
#  v 1.3
# This tries to read all the images in a dir 
# moves the corrupted files into an ERROR dir  


import os
from PIL import Image
import shutil  # To move the error file 

DIR = '../data/'
ERROR_DIR = '../ERROR_IMG/'

for filename in os.listdir(DIR):
    
  try:
    img = Image.open(DIR+filename)
    img.verify()
  except  Exception as e1 :
    print("Exception:" + str(e1)) 
    # move this file to an error directory 
    # create the directory if it does not exist
    if not os.path.isdir(f'{ERROR_DIR}'):
        print(f'creating ... {ERROR_DIR}')
        os.mkdir(f'{ERROR_DIR}')
    print(f'Mmoving file ...{filename} to {ERROR_DIR}')    
    shutil.move(DIR+filename,ERROR_DIR+filename)

