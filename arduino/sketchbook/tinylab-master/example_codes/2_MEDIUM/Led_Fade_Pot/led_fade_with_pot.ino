/*
 Fade for tinylab

 This example shows how to fade an LED on pin 10 and 11
 using the analogWrite() function. Turning on and off a light emitting diode(LED)  connected to digital pin 10 and 11.
 The amount of time the LED will be on and off depends on
 the value obtained by analogRead().

 This example code is in the public domain.

 modified 22 Jan 2016
 by Yasin Kaya (selengalp)
 */

int led1_pin = 11;   // the pin that the LED is attached to
int led2_pin = 10;   // the pin that the LED is attached to
int brightness = 0;  // how bright the LED is
int pot_pin =0;		 //the pin that the Potantiometer is attached to
int pot_value = 0;		

// the setup routine runs once when you press reset:
void setup() {
   // declare pin 10 an 11 to be an output:
   pinMode(led1_pin, OUTPUT);
   pinMode(led2_pin, OUTPUT);
   
   pinMode(pot_pin, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
	// reading pot. value 
  pot_value = analogRead(pot_pin);
  // calcualting PWM value that configures LED brightness
  brightness = pot_value * (255.0/1024.0);
  
  // pwm outputs 
  analogWrite(led1_pin, brightness);
  analogWrite(led2_pin, brightness);
  delay(30);
}

