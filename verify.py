import os
from PIL import Image
DIR = '../images/Uninfected/'
for filename in os.listdir(DIR):
  img = Image.open(DIR+filename)
	  try:
		  img.verify()
		except e1 as Exception  :
			print("Exception:" + str(e1))	
