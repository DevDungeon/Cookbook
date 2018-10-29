/*
  Analog Input
 Demonstrates analog input by reading LM35 temperature sensor on analog pin 3 and
 calculates temperature. Then temperature shows on serial monitor.

 Created by David Cuartielles
 modified 21 Jan 2016
 By Yasin Kaya (selengalp)

 */

int LM35_pin = A2;    // select the input pin
float temp = 0;  // variable to store the value coming from the sensor

void setup() {
	// opening serial monitor with 9600 boudrate
	Serial.begin(9600);
 	//setup pin direciton
 	pinMode(LM35_pin,INPUT);
 }

void loop() {
	// read the value from the sensor:
	int temp = ((2500.0 / (analogRead(LM35_pin) * (5.0 / 1024.0))) - 500) / 10.0; 
	// printing temperature to serial monitor 
	Serial.print("Temperature:   ");
	Serial.println(temp);
	delay(1000);
}
