# microbitDataGatherer
This repository is here to support my blog: 

It includes a series of microPython files that demonstrate the following:

<b> 1 = Applying the No-sleep Pragmatic Data Collection technique to collect data on your micro:bit</b></br>
<b> 2 = Using pattern recognition to identify interesting parts of the data</b></br>
<b> 3 = Transferring a large amount of data from 1 micro:bit, via an XinaBox micro:bit gateway, to an IoT platform</b></br>


<h1>Applying the No-sleep Pragmatic Data Collection technique</h1>
As I point out in my blog, the naming of this is very tongue-in-cheek.  I am sure the technique will have been used many times before I came along.  I couldn't find a mention of it though, so for now I claim naming rights!



Collect up to 150 data points on 1 micro:bit, then later transmit that data via radio to a 'micro:bit gateway'- a micro:bit with the XinaBox IoT Starter (Wi-fi) attached - which transmits it to an MQTT IoT platform - Ubidots in the code.

<b>Whats the Objective?</b></br>
... imagine a situation where the need arises to collect a large number of data points on a micro:bit</br>
... but the circumstances preclude extracting that data in real time.</br>
For example:</br>
... you have a wearable device (say a heart monitor) on you that takes readings you want to later extract.
... you are taking readings on a moving object</br>
... you want to leave a sensor array somewhere in nature to take intermittent readings overnight, which you will collect in the morning</br>

So, you collect these data points on 1 micro:bit then later trigger the data to be transmitted via radio towards any gateway that might be listening.  If it gets picked up by a gateway it gets sent on to the IoT platform.

Use the microPython code <b>RC_DataCollector</b> on the micro:bit you are using to sample data.<br>
You will need to adapt the code to accomodate the readings you are taking<br>
Its set up currently to take an accelerometer reading every 25ms (which is OK for testing)
Click A-button to initiate.  You get a count-down from 3, then it starts taking readings.
You get IMAGENAME when done.
Now you wait till you are next to a micro:bit gateway, then you click the B-button to transmit the array data.

Notes:.<br>
... I've written to a list, rather than to the file system.  It was easier for me is all.<br>
... there are potential optimisations aplenty - get the sleeps down, coordinate them better and look at queues / list length.
