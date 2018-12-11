import re
import math
import numpy as np
import pytesseract
from PIL import Image

# INPUT_FILE = "./input-example.txt"
INPUT_FILE = "./input.txt"


def place_point(img, x, y):
    placed = False
    real_x = (GRID_SIZE_W // 2) + x
    real_y = (GRID_SIZE_H // 2) + y
    if (real_x >= 0 and real_x < GRID_SIZE_W) and (real_y >= 0 and real_y < GRID_SIZE_H):
        img[real_y, real_x] = (0, 0, 0)
        placed = True

    return placed


points = [{
    "coords": {
        "x": int(m[0]),
        "y": int(m[1])
    },
    "velocity": {
        "x": int(m[2]),
        "y": int(m[3])
    }} for m in [re.findall("[-]?\d+", l) for l in open(INPUT_FILE)]]


GRID_SIZE_W = math.floor(len(points) * 1.5)
GRID_SIZE_H = math.floor(len(points) * 1.5)

found = False
time_elapsed = 0

while not found:
    time_elapsed += 1
    placed = False
    img = np.zeros([GRID_SIZE_W, GRID_SIZE_H, 3], dtype=np.uint8)
    img.fill(255)

    for p in points:
        p["coords"]["x"] += p["velocity"]["x"]
        p["coords"]["y"] += p["velocity"]["y"]

        placed = place_point(img, p["coords"]["x"], p["coords"]["y"])

    if placed:
        im = Image.fromarray(img)
        text = pytesseract.image_to_string(im)

        if text:
            print("Seconds waited: {}".format(time_elapsed))
            print("Message: {}".format(text))
            found = True
