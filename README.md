arduino_encoder
===============

Python tools for generating Arduino sketches as part of a Unix tool chain.

Usage
=====

`./encoder.py *module* > outputdir/output.ino`

(The Arduino software seems to prefer that .ino files be wrapped in an appropriately named directory- you're free just create a file, 
in which case the IDE will prompt you to relocate it into a directory)

The encoder reads from stdin and writes to stdout by default, so you can do standard things like:

`cat message.txt | ./encoder.py *module* > output.ino`

etc.

Sample Use: Morse Encoding
==========================
As a simple sample, I wrote a morse code encoder based on this tutorial: http://arduino.cc/en/Hacking/LibraryTutorial

Running `encoder.py morse_encoder` allows you to create a sketch file that will cause the Arduino Uno's LED to flash out an
arbitrary message in Morse code. The sample in sample.ino flashes out 'SOS This is only a test SOS'.

The generated code aims to be at least basically readable, and pauses between each word and at the end of lines.
You can adjust the timing of the dots, dashes, and gaps by altering the numbers in morse_encoder.py.

You can easily use Python together with template files, etc., to create an encoder that will allow you to create whatever behavior you want
in the Arduino board that can be driven from a fixed text message- sounds, light displays, driving the DA output, etc.
