/*
Physical notifier


*/


int redLed = 9;
int orangeLed = 10;
int greenLed = 11;
int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by

void setup()
{
  // Start serial port at 9600 bps and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  
  // Setup LEDs
  pinMode(greenLed, OUTPUT);
  pinMode(orangeLed, OUTPUT);
  pinMode(redLed, OUTPUT);
}

void loop()
{
  
  // SERIAL STUFF
  char inByte;
  if (Serial.available() > 0) 
  {
    inByte = Serial.read();
    Serial.print(inByte);
  } else {
    // Serial.println("No serial data available.");
  }
  
  
  // LED STUFF 
  analogWrite(greenLed, brightness);
  analogWrite(orangeLed, brightness);    
  analogWrite(redLed, brightness);    

  // change the brightness for next time through the loop:
  brightness = brightness + fadeAmount;

  // reverse the direction of the fading at the ends of the fade: 
  if (brightness == 0 || brightness == 255) {
    fadeAmount = -fadeAmount ; 
  }    
  
    delay(30);
  
  
}
