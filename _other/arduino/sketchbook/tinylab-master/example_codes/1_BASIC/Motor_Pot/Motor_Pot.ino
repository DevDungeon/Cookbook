/*
 * Driving DC motor for tinylab
 * created 22 Jan 2016
 * by Yasin Kaya (selengalp)
 */
int motor_pin = 5; // set the DC motor pin
int pot_pin = A0;  // set the potantiometer pin
int pot_value = 0;

void setup() {
  // setup pin direction
  pinMode(motor_pin,OUTPUT);
  // opening serial port with 9600 boudrate
  Serial.begin(9600);
}

void loop() {
 // reading potantiometer value
 pot_value = analogRead(pot_pin);

 // driving motor on desired velocity  
 analogWrite(motor_pin, pot_value);
}
