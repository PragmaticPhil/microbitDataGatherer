from microbit import *
import radio

#   This is inspired by Bjarke Gotfredsen who wrote the initial connection code, and many of his original lines remain here

radio.on()
radio.config(length=16, queue=64, channel=11, power=6)
#   NOTE: radio settings are identical to those in the classroomMicrobit.py code.  Long queue is necessary as we process each slowly

uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin20, rx=pin19)
# NOTE: gets the uart (serial / USB) port on the micro:bit ready to communicate with the CW01


def sendMessageToCW01(parm):        #   TODO - parametise the sleeps - seems to fail on startup with quicker ones, but not later.  Choke more early on.
    display.clear()
    uart.write(parm)
    sleep(250)
    data = uart.readline()
    while(data is None):
        data = uart.readline()
    
    if(len(str(data)) >0):
        uartMessageID = getIntegerFromString(data[:1])
        if(uartMessageID == 1):     display.show(Image.YES)     # NOTE: a tick is displayed when data is being transmitted correctly to the CW01
        else:                       display.show(Image.NO)      # NOTE: this means that a cross is displayed when an attempt to send data fails

    sleep(250)


def processRadioSignal(radioSignal):
    global testMode
    
    if(len(str(radioSignal)) < 4):   return False                       #   NOTE: valid radio signals are at least 4 or more characters long
    
    locationOfUnderscore = getLocationOfUnderscore(radioSignal)
    if(locationOfUnderscore == -1): return False                        #   NOTE: valid radio signals contain an underscore    

    currentMicrobitID = getIntegerFromString(radioSignal[0:locationOfUnderscore])
    if(currentMicrobitID < 0):    return False                          #   NOTE: valid radio messages begin with an integer starting at 0.
    if(currentMicrobitID > 9): return False                             #   NOTE: IDs should go from 0 to 9
 
    #   NOTE: If we've reached this point of the code the radioSignal has passed all our validation checks.  It is 'safe' to process it.
    return sendValidMessageToCW01(radioSignal, locationOfUnderscore)

def sendValidMessageToCW01(radioSignal, locationOfUnderscore):
    messageType = str(radioSignal[locationOfUnderscore +1 : locationOfUnderscore +2])
    
    if(messageType == "a"):
        sendMessageToCW01("+4@YOURMICROBIT@duration@" + getValueFromRadioSignal(radioSignal, locationOfUnderscore) + "$")
        return True

    if(messageType == "b"):
        sendMessageToCW01("+4@YOURMICROBIT@speed@" + getValueFromRadioSignal(radioSignal, locationOfUnderscore) + "$")
        return True

    if(messageType == "c"):
        sendMessageToCW01("+4@YOURMICROBIT@AccReading@" + getValueFromRadioSignal(radioSignal, locationOfUnderscore) + "$")
        return True
    
    return False
    

def getLocationOfUnderscore(radioSignal):
    #   NOTE: The underscore can only be in 1 of 2 places in the string, so KISS:
    radioSignalStr = str(radioSignal)
    if(radioSignalStr[1:2] == "_"):    return 1
    if(radioSignalStr[2:3] == "_"):    return 2
    return -1


def getIntegerFromString(uncheckedString):
    try: return int(uncheckedString)
    except ValueError: return -1


def getValueFromRadioSignal(radioSignal, locationOfUnderscore):
    #display.show(str(radioSignal[locationOfUnderscore +2 : len(radioSignal)]))
    try: return str(radioSignal[locationOfUnderscore +2 : len(radioSignal)])
    except: return "0"

#   INIT:

display.show(Image.SQUARE)          # NOTE: the square is shown on your micro:bit while it is connecting to Ubidots
sleep(2000)
uart.write("$")                     # NOTE: Cleans out the serial buffer
sleep(100)
uart.write("+9@?$")                 # NOTE: Reboots the CW01
sleep(5000)                         # NOTE: long delay is necessary - we need to give Wi-Fi time to sort itself out.
uart.write("$")                     # NOTE: Clean out Serial buffer, again.
sleep(500)

sendMessageToCW01("+1@WIFINAME@WIFIPASSWORD$")
# EDIT GUIDELINES: you MUST enter the name and password of the Wi-Fi network you are trying to connect to in the line above.

sendMessageToCW01("+2@DEFAULTTOKEN@?$")
# EDIT GUIDELINES: you MUST enter the DEFAULT TOKEN from Ubidots in the line above.

sendMessageToCW01("+3@things.ubidots.com@1883$")
# NOTE: above line tells the micro;bit where to send the data to - its a Ubidots URL.

sendMessageToCW01("+6@/v1.6/devices/microbit/number/lv$")
# NOTE: above is an ID for our CW01 - you can leave it as is.

sendMessageToCW01("+4@YOURMICROBIT@SummaryOfVote@-1$")
# NOTE: This variable is used to trigger an email sent after the vote - we set it to -1 as any value > -1 triggers the email.

while True:
    if(processRadioSignal(radio.receive())):    
        display.show(Image.HAPPY)               #   sadly this won't be seen for long at all.  Sleeps are built in to the sub routines so we don't need one
    else:
        display.show(Image.SAD)
        sleep(50)