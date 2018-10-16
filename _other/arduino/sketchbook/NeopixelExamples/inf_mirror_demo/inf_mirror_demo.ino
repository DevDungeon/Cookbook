#include <Adafruit_NeoPixel.h>

#define PIN 2
#define NUM_PIXELS 12

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_PIXELS, PIN, NEO_GRB + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {
  int numLoops = 2;
  for (int loopCount = 0; loopCount < numLoops; loopCount++) {
    staggerOnOff(500, 10);
  }
  for (int loopCount = 0; loopCount < numLoops; loopCount++) {
    doComet(200, 3);
  }
  for (int loopCount = 0; loopCount < numLoops; loopCount++) {
    doRainbow(25);
  }
  for (int loopCount = 0; loopCount < numLoops; loopCount++) {
    doRandom(200, 20);
  }
}


// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
   return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else if(WheelPos < 170) {
    WheelPos -= 85;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  }
}

void setAllOff() {
  for (int i = 0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, 0, 0, 0);
  }
  strip.show();
}

void doRandom(uint16_t wait, int count) {
  uint16_t i, j;
  for(j=0; j<count; j++) {
    for(i=0; i<strip.numPixels(); i++) {
      //strip.setPixelColor(i, Wheel((i+j) & 255));
      strip.setPixelColor(i, Wheel((i+random(256)) & 255));
    }
    strip.show();
    delay(wait);
  }
}

void doRainbow(uint16_t wait) {
  uint16_t i, j;
  for(j=0; j<256; j++) {
    for(i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
    }
    strip.show();
    delay(wait);
  }
}


void staggerOnOff(uint16_t wait, int count) {
  setAllOff();
  for (int offset = 0; offset < count; offset++) {
    for (int i = 0; i < strip.numPixels(); i++) {
      if ((i + offset) % 2 == 0) {
        strip.setPixelColor(i, 255, 0, 255);
      } else {
        strip.setPixelColor(i, 0, 0, 0);
      }
    }
    strip.show();
    delay(wait);
  }
}

void doComet(uint16_t wait, int cometTrailLength) {
  int trailPin;
  // Move the comet head from pixel 0 to the last pixel
  for (int leadPixel = 0; leadPixel < strip.numPixels(); leadPixel++) {
    // Set the pixels starting at the leadPixel (head of comet)
    setAllOff();
    for (int i = 0; i < cometTrailLength; i++) {
      trailPin = leadPixel - i;
      if (trailPin < 0) {
        trailPin = trailPin + strip.numPixels();
      }
      int brightness = 255 - ((255 / cometTrailLength) * i);
      strip.setPixelColor(trailPin, 0, brightness, 0);
    }
    strip.show();
    delay(wait);
  }
}

