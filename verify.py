#Created : 27 Mar 2022 
# This tries to read all the images in a dir 
# and gives an error when it is not able to open ( mostly because its corrupted while downloading )

# To do : Display the error / exception type / message 

import os
from PIL import Image

DIR = '../data/eval_all/'

try:
  for filename in os.listdir(DIR):
    img = Image.open(DIR+filename)
    img.verify()
except : # e1 as Exception :
  #print("Exception:" + str(e1)) 
  print(filename)


