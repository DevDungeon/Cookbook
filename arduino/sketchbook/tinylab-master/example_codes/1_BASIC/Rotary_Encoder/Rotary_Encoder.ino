// Read RotaryEncoder state for tinylab
// SimplePollRotator.ino - Example for the RotaryEncoder library.
// This class is implemented for use with the Arduino environment.
// Copyright (c) by Matthias Hertel, http://www.mathertel.de
// This work is licensed under a BSD style license. See http://www.mathertel.de/License.aspx
// More information on: http://www.mathertel.de/Arduino
// -----
// 18.01.2014 created by Matthias Hertel
// 22.01.2016 modified by Yasin Kaya (selengalp) 
// -----

// This example checks the state of the rotary encoder in the loop() function.
// The current position is printed on output when changed.


#include <RotaryEncoder.h>


RotaryEncoder tinyEncoder(6, 7);

void setup()
{
	// openserial port 
  Serial.begin(9600); 
}


// Read the current position of the encoder and print out when changed.
void loop()
{
  
  static int pos = 0;
  tinyEncoder.tick();

  int newPos = tinyEncoder.getPosition();
  
  if(pos != newPos){ 
    Serial.print("Rotary Position:   ");
    Serial.println(pos);
    pos = newPos;
  }
}



