# microbitDataGatherer
This repository is here to support my blog:  http://pragmaticPhil.co.uk/2019/03/16/data-capturing-on-the-microbit/

Collect up to 150 data points on 1 micro:bit, then later transmit that data via radio to a 'micro:bit gateway'- a micro:bit with the XinaBox IoT Starter (Wi-fi) attached - which transmits it to an MQTT IoT platform - Ubidots in the code.

<b>Whats the Objective?</b></br>
<ul>  
<li>... imagine a situation where the need arises to collect a large number of data points on a micro:bit</li>
<li>... but the circumstances preclude extracting that data in real time.</li>
</ul>
For example:</br>
... you have a wearable device (say a heart monitor) on you that takes readings you want to later extract.
... you are taking readings on a moving object</br>
... you want to leave a sensor array somewhere in nature to take intermittent readings overnight, which you will collect in the morning</br>

This repo includes 2 files that demonstrate the following:

<b> 1 = Applying the No-sleep Pragmatic Data Collection technique to collect data on your micro:bit</b></br>
<b> 2 = Using pattern recognition to identify interesting parts of the data</b></br>

My use case also requires me o transferg a large amount of data from 1 micro:bit, via an XinaBox micro:bit gateway, to an IoT platform.  I will be writing a Hackster how-to that covers this</b></br>


<h3>Applying the No-sleep Pragmatic Data Collection technique</h3>
As I point out in my blog, the naming of this is very tongue-in-cheek and I am sure the technique will have been used many times before I came along.  I couldn't find a mention of it though, so for now I claim naming rights!</br>

The technique is described in detail on the blog - I won't repeat here.  To check it operating for yourself follow the steps below: </br>
<ul>
<li>Flash the <b>data_MAcollector.py</b> file onto a micro:bit.</li>
<li>Push the A-button to initiate the data reading process.</li>
<li>After the countdown finishes the micro:bit will read accelerometer data for about 2.5 seconds.  A single dot is shown on screen during this period.</li>
<li>When the readings have completed you can press the B-button to see how many times we sampled the accelerometer during every data collection cycle.</li>
</ul>

<h3>Identifying patterns in the data</h3>

The microPython code <b>data_StartStopPt</b> shows this technique </br>
I've hard-coded a data set with 80 data points to demonstrate how it works.  These are 'real' values taken from the real world application I am working on. </br>

More detail on why it is necessary, and how it works, can be found on the blog linked to above.

Flash the code onto a micro:bit, then:
<ul>
<li>Click A-button:  This shows you the data point where the first pattern of accelerating values starts.</li>
<li>Click B-button:  This shows you the data point where the last pattern of accelerating values starts.</li>  
</ul>

