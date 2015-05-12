"""
A test of the ability to generate a JPG based on an array of boolean values.
Works with Python 2.7
For Game Of Life
"""
from PIL import Image
import random
file = open('Saved Images/as.txt', 'r+')
length = str(len(file.read()))
file.write('a')
file.close()

def printarray():
    for x in array:
        print x

size = 10
array = [[False for _ in range(size)] for _ in range(size)]
img = Image.new("RGB", (size, size), "white")
pixels = img.load()
for x in range(size):
    for y in range(size):
        if random.randint(0, 1):
            array[x][y] = True

for x in range(size):
    for y in range(size):
        if array[x][y] == True:
            pixels[x, y] = (0, 0, 0)

img.save('Saved Images/Saved_Pattern_' + length + '.jpg')

