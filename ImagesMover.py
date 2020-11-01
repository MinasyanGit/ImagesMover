import shutil
import glob
jpeg_file = glob.glob("/Users/levon/Desktop/*.jpeg")
jpg_file = glob.glob("/Users/levon/Desktop/*.jpg")
png_file = glob.glob("/Users/levon/Desktop/*.png")


for file in jpeg_file:
    shutil.move(file, "/Users/levon/Desktop/images/" + file.split('/')[4])

for file in jpg_file:
    shutil.move(file, "/Users/levon/Desktop/images/" + file.split('/')[4])

for file in png_file:
    shutil.move(file, "/Users/levon/Desktop/images/" + file.split('/')[4])