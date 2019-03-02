import Image
import numpy as np
import sys
import os
np.set_printoptions(threshold=np.inf)      
height = 40
width = 40
#python LC_pythonBmpDecoder.py black.bmp black
img = Image.open(sys.argv[1]).convert('L')
a = np.array(img)
output = [hex(1)] * int((width / 8) * height)
for y in range(0,height):     #format the image
    for x in range(0,width):
        a[y][x]+=1
index = 0
for y in range(0,height):     #squeeze 8 numbers into 1 number
    x = 0
    while True:
        b = 0b00000000
        for i in range(0,8):
            if a[y][x + i] == 1:
                b = b + (0b00000001 << (7 - i))
        output[index] = hex(b)
        index = index + 1
        x = x + 8
        if x == 40 :
            break
inString = "const unsigned char gImage_" + sys.argv[2] + "[200] = {\n"
for i in range(0,200):
    inString += output[i]
    inString += ";"
    if i in [19,39,59,79,99,119,139,159,179,199]:
        inString += "\n"
inString += "};"
f = open(sys.argv[2]+".c","w")
f.write(inString)
f.close()
print(output)
print("C file have been created")

