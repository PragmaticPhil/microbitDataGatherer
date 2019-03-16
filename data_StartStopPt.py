from microbit import *

accReadingList = []

#   the code below was auto-generated in Excel and includes 80 data points, real data taken from accelerometer.get_y()

accReadingList.append(0)        #   0
accReadingList.append(0)
accReadingList.append(0)
accReadingList.append(0)
accReadingList.append(0)
accReadingList.append(0)
accReadingList.append(12.8)
accReadingList.append(0)
accReadingList.append(-6.4)     #   8   = start of first pattern of increase
accReadingList.append(19.2)
accReadingList.append(51.2)
accReadingList.append(179.2)
accReadingList.append(422.4)
accReadingList.append(614.4)
accReadingList.append(896)
accReadingList.append(1574.4)
accReadingList.append(1881.6)
accReadingList.append(2694.4)
accReadingList.append(2969.6)
accReadingList.append(3718.4)
accReadingList.append(3980.8)   #   20
accReadingList.append(4633.6)
accReadingList.append(3859.2)
accReadingList.append(3078.4)
accReadingList.append(2643.2)
accReadingList.append(2483.2)
accReadingList.append(1049.6)
accReadingList.append(1529.6)
accReadingList.append(1619.2)
accReadingList.append(1094.4)
accReadingList.append(198.4)    #   30
accReadingList.append(390.4)
accReadingList.append(-281.6)
accReadingList.append(-608)
accReadingList.append(-876.8)
accReadingList.append(-998.4)
accReadingList.append(-1299.2)
accReadingList.append(-1824)
accReadingList.append(-1683.2)
accReadingList.append(-1606.4)
accReadingList.append(-1452.8)  #40
accReadingList.append(-518.4)
accReadingList.append(-51.2)
accReadingList.append(-428.8)
accReadingList.append(-614.4)
accReadingList.append(-134.4)
accReadingList.append(-1158.4)
accReadingList.append(-1171.2)
accReadingList.append(-588.8)
accReadingList.append(-448)
accReadingList.append(-902.4)   #50
accReadingList.append(-454.4)
accReadingList.append(-339.2)
accReadingList.append(-96)
accReadingList.append(166.4)
accReadingList.append(-25.6)
accReadingList.append(160)
accReadingList.append(44.8)
accReadingList.append(-6.4)
accReadingList.append(-556.8)
accReadingList.append(-640)     #   60
accReadingList.append(-1043.2)
accReadingList.append(-1145.6)
accReadingList.append(-889.6)
accReadingList.append(-454.4)
accReadingList.append(96)
accReadingList.append(-140.8)
accReadingList.append(-774.4)
accReadingList.append(-2054.4)
accReadingList.append(-2995.2)  #   Start of LAST pattern of increase
accReadingList.append(-2956.8)  #   70
accReadingList.append(-2393.6)
accReadingList.append(-1664)
accReadingList.append(-608)
accReadingList.append(12.8)
accReadingList.append(38.4)
accReadingList.append(326.4)
accReadingList.append(12.8)
accReadingList.append(0)
accReadingList.append(0)
accReadingList.append(0)    #   80


def findStartReference(accReadingList):      #  Find the data point where the first 'pattern' in the data set begins
    #   Here we find the first place in the data where acc readings increase over 5 data points:
    readingCheckRef = 0
    
    while(readingCheckRef < (len(accReadingList) - (6))):     #   infinite recursion risk mitigated in checkPatternRecursions. 6 = pattern length + 1
        nextCheckIncrement = checkPatternRecursions(readingCheckRef, 5, 1, accReadingList)
        if(nextCheckIncrement == -1): return readingCheckRef    #   any value > 0 means we have NOT found the pattern we were looking for.
        readingCheckRef += nextCheckIncrement                   #   the positive value returned is the step where the pattern 'failed'
    
    return -9       #   Means no starting point was found (-9 helps in testing - distinquishes it from -1).


def findEndReference(accReadingList, startPoint):   #   Here we need to find where the last increase begins.
    patternRef = 0                      #   we could start at the end, work back until we find a pattern, then work back to where it begins.
                                        #   That would be the clever way.  But I am going for the easy way:
    #   Rem - we want to find the Start of the last pattern of sustained increase... 
    listPointer = startPoint
    
    while(listPointer < len(accReadingList) - 5):   #   we go for brute force - work through ALL the data point 1-by-1 recording pattern starts.
        patternStart = checkPatternRecursions(listPointer, 1, 5, accReadingList)
        listPointer += 1
        if(patternStart == -1):           #   a pattern has been found.  Rem - by definition we may find that the next point is also a pattern start.
            patternRef = listPointer       #   record where the pattern starts.

    return findCurrentPatternStart(patternRef, 1 ,5, accReadingList)    # finds where current pattern starts


def findCurrentPatternStart(startRef, patternInt, patternLength, accReadingList):
    #   Here we have found a point on the last pattern, BUT if is is part of a LONGER pattern our reference is not the start point of that.
    #   So, we work backwards (in the data set) from the point we found above to find where the pattern starts:
    patternFound = True
    
    while(patternFound and startRef > 1):
        startRef += -1
        if(checkPatternRecursions(startRef, patternInt, patternLength, accReadingList) > 0):    #   no pattern found = success!
            return (startRef + 1)
            
    return -1
    

def checkPatternRecursions(startRef, patternLength, patternInt, accReadingList):
    #   we are going to iterate patternLength times through values adjacent to accReadingList[startRef] and check whether there is a consistent change
    #   in acceleration in the direct 1*patternInt  (note - patternInt is 1 or -1)
    #   we should return a bool, but if we fail to detect a pattern it makes sense to communicate where it broke, so next time this is called
    #   we can start at the break, rather than repeat the checking of the values leading up to the break.
    #   We'll return -1 to indicate a successful pattern detection.
    
    for i in range(0, patternLength):
                
        fitsPattern = patternInt * (accReadingList[startRef + i+1] - accReadingList[startRef + i]) 
        #   fitsPattern > 0 means:
        #   ... if patternInt = -1 and PointDif < 0 we are decelerating and looking for a decelerating pattern.
        #   ... if patternInt = 1 and PointDif > 0 we are accelerating and looking for an accelerating pattern.
        #   fitsPattern < 0
        #   ... if patternInt = 1 and PointDif < 0 we are decelerating and looking for an accelerating pattern.
        #   ... if patternInt = -1 and PointDif > 0 we are accelerating and looking for an decelerating pattern.
        
        #   SO... when fitsPattern <0 we know that our pattern is not observed, so we do an early exit:        
        if(fitsPattern <= 0):    return (i+1)    #   i+1 ensures we don't get stuck in an infinite recurrsion in findStartReference
        
    #   At this point we've checked patternLength adjacent values and no exception to the pattern has been found, so a pattern exists.
    #   we return -1 to indicate we found the pattern:
    return -1   
   

while True:
   
    if(button_a.was_pressed()): display.show(str(findStartReference(accReadingList)))
    if(button_b.was_pressed()): display.show(str(findEndReference(accReadingList, 5)))
