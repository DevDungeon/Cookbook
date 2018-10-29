/*
  Analog Input
 Reading LDR light sensor on analog pin 2 and
 Lux is calculating. Then light value shows on serial monitor.

 Created by David Cuartielles
 modified 21 Jan 2016
 By Yasin Kaya (selengalp)

 */

int LDR_PIN = A2;  // select the input pin
float light = 0;  // variable to store the value coming from the sensor

void setup() {
  // opening serial monitır with 9600 boudrate 
  Serial.begin(9600);
  // setup pin direction
  pinMode(LDR_PIN,INPUT);
}

void loop() {
  // read the value from the sensor:
  int light = ((2500.0 / (analogRead(LDR_PIN) * (5.0 / 1024.0))) - 500) / 10.0; 
  // printing lux value to serial monitor
  Serial.print("Lux:   ");
  Serial.println(light);
  delay(1000);
}
