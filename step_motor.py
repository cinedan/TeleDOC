from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

try:
    Pin23 = GP.getPin23()
    Pin23.out()

    Pin25 = GP.getPin25()
    Pin25.out()	

    Pin27 = GP.getPin27()
    Pin27.out()

    Pin31 = GP.getPin31()
    Pin31.out()	

    print("Pins are set to output")
    
    for i in range(0,20):
        if Pin23.getValue() == 1:
            Pin23.low()
            Pin25.high()
        elif Pin25.getValue() == 1:
            Pin25.low()
            Pin27.high()
        elif Pin27.getValue()  == 1:
            Pin27.low()
            Pin31.high()
        elif Pin31.getValue()  == 1:
            Pin31.low()
            Pin23.high()
        else:
            Pin25.high()
        time.sleep(1)

finally:
    GP.cleanup()
