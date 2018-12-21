from PIL import Image
from numpy import array
from time import sleep
import sys

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def get_image_brightness():
    img = Image.open("superstition.jpg")
    width, height = img.size[0], img.size[1]

    img = img.load()

    char_array = [[i for i in range(0,width)] for x in range(0,height)]
    row = 0
    column = 0
    while column < width:
        while row < height:
            pixel = img[column, row]
            average = int((pixel[0]+pixel[1]+pixel[2])/3)
            char = int(round((average/255)*64))
            char_array[row][column] = chars[char]
            row+=1
        column+=1
        row = 0
    return char_array

char_array = get_image_brightness()
for line in char_array:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.write(char)
    print('\r')
