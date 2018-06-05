/*
  Analog Input for tinylab
 Demonstrates analog input by reading an analog pot on analog pin 0.


 Created by David Cuartielles
 modified 22 Jan 2016
 By Yasin Kaya (selengalp)

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/AnalogInput

 */

int pot_pin = A0;    // select the input pin for the potentiometer
int pot_value = 0;  // variable to store the value coming from the pot

void setup() {
	// setup pin direction 
	pinMode(pot_pin, INPUT);
	// open serial port 
	Serial.begin(9600);

}

void loop() {
  // read the value from the pot:
  pot_value = analogRead(pot_pin);
  // print the potantiometer value to serial monitor
  Serial.print("Potantiometer: ");
  Serial.println(pot_value);
  delay(100);
  
}
