"""
A test of the ability to read a JPEG of black and white pixels, and create
an array based on that.
Works with Python 2.7
For use with Game of Life
"""
from PIL import Image

def printarray2():
    for x in array2:
        print x
def printarray():
    for x in array:
        print x

img = Image.open("Saved Images/smalltest.jpg")
if img.size[0] == img.size[1]:
    size = img.size[0]
else:
    print "STUFF AND THINGS"

array = [[False for _ in range(size)] for _ in range(size)]
array2 = [[(0, 0, 0) for _ in range(size)] for _ in range(size)]

pixels = img.load()

for x in range(size):
    for y in range(size):
        array2[x][y] = pixels[y, x]

for x in range(size):
    for y in range(size):
        if array2[x][y][0] >= 100 and array2[x][y][1] >= 100 and array2[x][y][2] >= 100:
            array[x][y] = False
        else:
            array[x][y] = True
printarray()
