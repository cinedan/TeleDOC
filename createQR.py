import pyqrcode
import sys
#import pypng

if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit("ERROR! Two args required")
    else:
        qr = pyqrcode.create(sys.argv[1])
        #with open('zbar-test.png', 'w') as fstream:
        qr.png(sys.argv[2], scale=5)
            
