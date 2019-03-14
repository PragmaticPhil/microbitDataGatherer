from microbit import *

accReadingList = []

startingTime = 0
duration = 0

startTiming = False

totalNumberOfReadings = 150
numberOfReadings = 0

maxReadingsPerCycle = 0

while True:

    if(button_a.was_pressed()): 
        display.show("3")
        sleep(500)
        display.show("2")
        sleep(500)
        display.show("1")
        sleep(500)
        display.show(".")
        startTiming  = True
        startingTime = running_time()
        
    if(startTiming):
        #   We have 25ms (or whatever u change it to) to get an accelerometer reading... we might as well use that time productively.
        #   So, what we'll do is sample the acc reading 5 times during this loop, and we'll record the average value across those readings.
        #   This 'moving average' will help to smooth out any erratic readings.
        
        loopStart = running_time()  #   record the time now, so we can stop the loop below after 25ms
        accSmoothReading = 0        #   we'll use this to find the sum of all readings during our 25ms
        accSmoothReadings = 0       #   and we count how many readings we are able to make.
        
        
        while(  (loopStart + 25) > running_time() ):
            accSmoothReading += accelerometer.get_y()
            accSmoothReadings += 1
        
        
        if(accSmoothReadings > 0):
            accMovingAverage = accSmoothReading / accSmoothReadings
            accReadingList.append(accMovingAverage)
            if(maxReadingsPerCycle < accSmoothReadings):    maxReadingsPerCycle = accSmoothReadings
            numberOfReadings += 1
       
        
        
    if((numberOfReadings >= totalNumberOfReadings) and startTiming): 
        startTiming = False
        duration = running_time() - startingTime
        display.clear()
        sleep(500)
        
    if(button_b.was_pressed()):
        display.show(str(maxReadingsPerCycle) + "_")
        sleep(1000)