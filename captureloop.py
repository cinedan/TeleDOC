import qrcode
import capture

def getQRcode(devNum=0, loopLength=10):
    decode = []
    count = 0
    while len(decode) == 0 and count < loopLength: # TODO: change to time interval
        img = capture.capture(vidDevNum=devNum, outName="")
        decode = qrcode.decode(img)
        # Print results
        # print(decode)
        # for obj in decode:
        #     print('Type : ', obj.type)
        #     print('Data : ', obj.data,'\n')
        count += 1
    if len(decode) != 0:
        # Print results
        # for obj in decode:
        #     print('Type : ', obj.type)
        #     print('Data : ', obj.data,'\n')
        return decode[0].data.decode('utf-8')
    else:
        return ""
    
if __name__ == '__main__':
    print(getQRcode())

