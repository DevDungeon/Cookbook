#include <Adafruit_NeoPixel.h>

#define NEOPIXEL_PIN            2
#define NUMPIXELS      30
int sensorPin = A0;    // select the input pin for the potentiometer


int sensorValue = 0;  // variable to store the value coming from the sensor
int sensorValue2 = 0;  // variable to store the value coming from the sensor
int buzzerPin = A1;

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, NEOPIXEL_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  pixels.begin();
}

void loop() {
  int pixelNum, i;
  
  for (i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, 0, 0, 0);
  }
  
  sensorValue = analogRead(sensorPin);
  Serial.println(sensorValue);
  
  pixelNum = (sensorValue / (1024 / (NUMPIXELS-1)));
  
  pixels.setPixelColor(pixelNum, 0, 0, 255);
  
  pixels.show();
  
  
  
  
  delay(1);
}
