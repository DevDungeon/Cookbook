#include <RotaryEncoder.h>

/*

*/
//

//const int rotaryAPin = 6;
//const int rotaryBPin = 7;
//const int led1 = 13;
//const int led2 = 12;
//const int led3 = 11;
//
//int buttonState = 0;
//int rotaryAState = 0;
//int rotaryBState = 0;
//
//void setup() {
//  pinMode(led1, OUTPUT);
//  pinMode(led2, OUTPUT);
//  pinMode(led3, OUTPUT);
//  pinMode(buttonPin, INPUT);
//  pinMode(rotaryAPin, INPUT);
//  pinMode(rotaryBPin, INPUT);
//}
//
//void loop() {
//  buttonState = digitalRead(buttonPin);
//  rotaryAState = digitalRead(rotaryAPin);
//
//
//  if (buttonState == HIGH) {
//    digitalWrite(led2, HIGH);
//  } else {
//    digitalWrite(led2, LOW);
//  }
//  if (rotaryAState == LOW) {
//    digitalWrite(led1, HIGH);
//  } else {
//    digitalWrite(led1, LOW);
//  }
//}

RotaryEncoder tinyEncoder(6, 7);
const int buttonPin = A5; // Rotary encoder on Arduino also has button.
int buttonState = 0;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
}

void loop() {
  static int position = 0;
  tinyEncoder.tick();
  int newPos = tinyEncoder.getPosition();
  if (position != newPos) {
    Serial.print("Rotary position:  ");
    Serial.println(position);
    position = newPos;
  }

  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    Serial.print("Button pressed!");
  }
}

