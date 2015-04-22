#include <SoftwareSerial.h>

SoftwareSerial mySerial(8, 9); // RX, TX


/*
Special Parallax LCD codes
8 - cursor left
9 - cursor right
10 - cursor down
128 to 143 - position cursor on line 1, character 0-15
148 to 163 - position cursor on line 2, character 0-15

12 - clear screen (requires pause 5)
13 - carriage return
17 - backlight on
18 - backlight off
21 - Turn off display
22 - Turn on display

212 - set up next note for quarter-note length
220 - sounds A (440Hz)

Space character to delete letter
*/

void setup()  
{
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }


  Serial.println("Goodnight moon!");

  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
  mySerial.println("Hello, world?");
}

void loop() // run over and over
{
  if (mySerial.available()) {
    Serial.write(mySerial.read());

  }
  if (Serial.available()) {
    mySerial.write(Serial.read());
    mySerial.write(212);
    mySerial.write(220);

  }
    
}

