from microbit import *
import radio
radio.on()
radio.config(length=16, queue=64, channel=11, power=6)

readingFrequencyInMS = 25
accReadingList = []

startingTime = 0
duration = 0

startTiming = False

totalNumberOfReadings = 150
numberOfReadings = 0

readyToTransmit = False


def showCountdown():
    display.show("3")
    sleep(500)
    display.show("2")
    sleep(500)
    display.show("1")
    sleep(500)
    display.show(".")
    

while True:
    
    if(readyToTransmit):    display.show(Image.HAPPY)
    
    if(button_a.was_pressed()): 
        readyToTransmit = False
        showCountdown()
        startTiming  = True
        startingTime = running_time()
        
    if(startTiming):
        #loopStart = running_time()
        accReadingList.append(accelerometer.get_x())
        numberOfReadings += 1
        sleep(readingFrequencyInMS)
       # while(  (loopStart + readingFrequencyInMS) < running_time() ):     #   TODO - This loop SHOULD enforce a readingFrequencyInMSms time limit per iteration...
       #     sleep(1)                                                       #   regardless of how long above code takes 2 process
        
    if((numberOfReadings >= totalNumberOfReadings) and startTiming): 
        startTiming = False
        readyToTransmit = True
        duration = running_time() - startingTime
        display.clear()
        sleep(500)
        
    if(button_b.was_pressed() and readyToTransmit):
        display.show(Image.YES)
        radio.send("0_a" + str(duration))
        for i in range(0, totalNumberOfReadings - 1):
            radio.send("0_c" + str(accReadingList[i]))
            display.show(Image.YES)
            sleep(50)
            if((i % 32) == 0):     
                display.show(Image.SQUARE_SMALL)
                sleep(7500)
                
            
