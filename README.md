# microbitDataGatherer
Collect up to 150 data points on 1 micro:bit, then later transmit that data via radio to a 'micro:bit gateway'- a micro:bit with the XinaBox IoT Starter (Wi-fi) attached - which transmits it to an MQTT to an IoT platform - Ubidots in the code.

Whats the Objective?</br>
... imagine a situation where the need arises to collect a large number of data points on a micro:bit</br>
... but the circumstances preclude extracting that data in real time.</br>
For example:
... you are taking readings on an object that is away from a source - such as a moving vehicle.
... you want to leave a sensor array somewhere in nature to take intermittent readings overnight, which you will collect in the morning

So, you collect these data points then (on B-button was_pressed) the data is transmitted via radio
... towards any gateway that might be listening

Note - I've written to a list, rather than to the file system.  
It was easier is all, and this is not meant to be robust, just a POC.
