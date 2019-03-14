from microbit import *

accReadingList = []             #   This is a list - we will add each accelerometer reading we take to this list.
totalNumberOfReadings = 150     #   The code is limited to 150 data points - a few more is possible but there is an upper limit
numberOfReadings = 0            #   I don't use a loop to do the 150 readings, so I count how many we've done and stop at 150

startingTime = 0                #   We time how long it takes (although this is a factor of totalNumberOfReadings and our sampling period)
duration = 0

startTiming = False             #   This is a switch we set to True when we are reading accelerometer data

maxReadingsPerCycle = 0         #   For interest we'll take note of the max number of readings we are able to make in 1 cycle.

def countDownValue(currentCount):       #   Just a little countdown to prepare the user for when the micro:bit begins measuring data.
    display.show(str(currentCount))
    sleep(500)

while True:

    if(button_a.was_pressed()):         #   Initiate the process of reading data
        countDownValue(3)
        countDownValue(2)
        countDownValue(1)
        display.show(".")
        startTiming  = True             
        startingTime = running_time()
        
    if(startTiming):
        #   We have 25ms (or whatever u change it to) to get an accelerometer reading... we might as well use that time productively.
        #   So, what we'll do is sample the acc reading as much as possible during this loop, and we'll record the average value across those readings.
        #   This 'moving average' will help to smooth out any erratic readings.
        
        loopStart = running_time()  #   record the time now, so we can stop the loop below after 25ms
        accSmoothReading = 0        #   we'll use this to find the sum of all readings during our 25ms
        accSmoothReadings = 0       #   and we count how many readings we are able to make.
        
        
        while(  (loopStart + 25) > running_time() ):        #   we stay in this loop for 25 ms
            accSmoothReading += accelerometer.get_y()       #   we add the accelerometer readings during this period
            accSmoothReadings += 1                          #   and we record the number of readings we are able to make.
        
        
        if(accSmoothReadings > 0):                          #   Unlikely we need this, but it means no risk of dividing by zero below.
            accMovingAverage = accSmoothReading / accSmoothReadings
            accReadingList.append(accMovingAverage)         #   ADD THE AVERAGE READING DURING THE 25ms PERIOD
            if(maxReadingsPerCycle < accSmoothReadings):    #   This is just to show us how many readings we manage per cycle.
                maxReadingsPerCycle = accSmoothReadings
            numberOfReadings += 1
       
        
        
    if((numberOfReadings >= totalNumberOfReadings) and startTiming):    #   Straight after 150 readings have been taken this switch is True
        startTiming = False
        duration = running_time() - startingTime
        display.show(Image.DIAMOND)
        sleep(500)
        
    if(button_b.was_pressed()):
        display.show(str(maxReadingsPerCycle) + "_")
        sleep(1000)