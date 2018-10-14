import sys
from cv2 import *

def capture(vidDevNum=0, outName="output.jpg"):
    cam = VideoCapture(vidDevNum) # 0 is camera index

    s, img = cam.read()
    if s:
        if outName != "":
            imwrite(outName, img)
        return img

if __name__ == '__main__':
    if len(sys.argv) < 3:
        capture()
    else:
        capture(vidDevNum=int(sys.argv[1]), outName=sys.argv[2])
