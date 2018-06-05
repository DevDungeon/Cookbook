/*
 Button and LED for tinylab

 Turns on and off a light emitting diode(LED) connected to digital
 pin 13, when pressing a pushbutton attached to pin 9.


 created 2005
 by DojoDave <http://www.0j0.org>
 modified 21 Jan 2016
 by Yasin Kaya

 */

// constants won't change. They're used here to
// set pin numbers:
const int button_pin = 9;     // the number of the pushbutton pin
const int led_pin =  13;      // the number of the LED pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(led_pin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(button_pin, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  button_state = digitalRead(button_pin);
  
  if (button_state == LOW) {
    // turn LED on:
    digitalWrite(led_pin, HIGH);
  }
  else {
    // turn LED off:
    digitalWrite(led_pin, LOW);
  }
}
