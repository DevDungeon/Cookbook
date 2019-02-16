#include <Adafruit_NeoPixel.h>

#define NEOPIXEL_PIN            2
#define NUMPIXELS      30
int sensorPin = A2;    // select the input pin for the potentiometer


int sensorValue = 0;  // variable to store the value coming from the sensor

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, NEOPIXEL_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  pixels.begin();
}

void loop() {
  int i;

  sensorValue = analogRead(sensorPin);
  Serial.println(sensorValue);
    
  int brightness = sensorValue - 768; // average brightness is 800 so only use the top 256 values as range
  for (i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, brightness, brightness, brightness);  
  }
    
  pixels.show();
  
  delay(1);
}
