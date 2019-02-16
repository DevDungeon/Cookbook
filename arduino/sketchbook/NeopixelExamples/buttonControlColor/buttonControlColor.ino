#include <Adafruit_NeoPixel.h>

const int buttonPin1 = 9;     // the number of the pushbutton pin
const int buttonPin2 = 8;     // the number of the pushbutton pin
const int buttonPin3 = A5;     // the number of the pushbutton pin
const int ledPin1 =  12;      // the number of the LED pin
const int ledPin2 =  11;      // the number of the LED pin
const int ledPin3 =  10;      // the number of the LED pin

// variables will change:
int buttonState1 = 0;         // variable for reading the pushbutton status
int buttonState2 = 0;         // variable for reading the pushbutton status
int buttonState3 = 0;         // variable for reading the pushbutton status

#define NEOPIXEL_PIN            2
#define NUMPIXELS      30

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, NEOPIXEL_PIN, NEO_GRB + NEO_KHZ800);


void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);

  pixels.begin();
}

void loop() {
  // read the state of the pushbutton value:
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState3 = digitalRead(buttonPin3);
  int red, green, blue, i;

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState1 == HIGH) {
    digitalWrite(ledPin1, HIGH);
    red = 0;
  } else {
    // turn LED off:
    digitalWrite(ledPin1, LOW);
    red = 255;
  }
    
  if (buttonState2 == HIGH) {
    digitalWrite(ledPin2, HIGH);
    green = 0;
  } else {
    digitalWrite(ledPin2, LOW);
    green = 255;
  }
  
  if (buttonState3 == LOW) {
    digitalWrite(ledPin3, HIGH);
    blue = 0;
  } else {
    digitalWrite(ledPin3, LOW);
    blue = 255;
  }

  for (i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, red, green, blue);
  }
  pixels.show();

  
   
}
