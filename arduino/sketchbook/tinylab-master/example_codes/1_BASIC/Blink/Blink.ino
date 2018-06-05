/*
  Blink for tinylab
  Turns on an LED on for one second, then off for one second, repeatedly.

  This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
  remodified 21 jan 2016
  by Onur Oktar
  */


// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 10 as an output.
  pinMode(10, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(10, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(10, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);              // wait for a second
}
