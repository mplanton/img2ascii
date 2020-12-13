#!/usr/bin/env python3
#
# Manuel Planton 2020
#
# usage:   python3 img2ascii.py <image-file> <line-width> <chars from dark to bright>
# example: python3 img2ascii.py face.jpg 160 " .*#"

import sys
from PIL import Image

def pix2char(pix, max_pix, chars):
    n = len(chars)
    for i in range(n):
        if pix <= max_pix * (i + 1) / n:
            return chars[i]

# line width
try:
    width = int(sys.argv[2])
except:
    width = 80

# characters from dark to bright
try:
    chars = sys.argv[3]
except:
    chars = " .\'*|$&#"

im = Image.open(sys.argv[1])
sz = im.size
factor = (sz[0] / width) * 2
height = int(sz[1] / factor)
sz = (width, height)
im = im.resize(sz).convert("L")
max_pix = im.getextrema()[1]

for row in range(height):
    line = ""
    for col in range(width):
            line += pix2char(im.getpixel((col, row)), max_pix, chars)
    print(line)

