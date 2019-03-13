# microbitDataGatherer
Collect up to 150 data points on 1 micro:bit, then later transmit that data via radio to a 'micro:bit gateway'- a micro:bit with the XinaBox IoT Starter (Wi-fi) attached - which transmits it to an MQTT IoT platform - Ubidots in the code.

<b>Whats the Objective?</b></br>
... imagine a situation where the need arises to collect a large number of data points on a micro:bit</br>
... but the circumstances preclude extracting that data in real time.</br>
For example:</br>
... you have a wearable device on you that takes readings you want to later extract.
... you are taking readings on an object that is away from a source - such as a moving vehicle.</br>
... you want to leave a sensor array somewhere in nature to take intermittent readings overnight, which you will collect in the morning</br>

So, you collect these data points then (on B-button was_pressed) the data is transmitted via radio towards any gateway that might be listening.

Use the microPython code "RC_DataCollector" on the micro:bit you are using to sample data.<br>
You will need to adapt the code to accomodate the readings you are taking<br>
Its set up currently to take an accelerometer reading every 25ms (which is OK for testing)

Notes:.<br>
... I've written to a list, rather than to the file system.  It was easier for me is all.<br>
... there are potential optimisations aplenty - get the sleeps down, coordinate them better and look at queues / list length.
