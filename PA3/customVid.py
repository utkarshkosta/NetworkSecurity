import cv2
import numpy as np
import glob
# from PIL import Image

images = []

width = 1280
height = 720

files = []

for file in glob.glob('images/*.jpg'):
	files.append(file)

files.sort(reverse = True)
# print(files)

for file in files:
	img = cv2.imread(file)
	# h,w,l = img.shape
	# size = (width, height)
	# img = Image.open(file)
	# img = img.resize((width, height))
	# img.save(file)
	images.append(img)


out = cv2.VideoWriter('custom.avi', cv2.VideoWriter_fourcc(*'HFYU'), 1, (width, height))

# print(images)

for image in images:
	out.write(image)

out.release()
