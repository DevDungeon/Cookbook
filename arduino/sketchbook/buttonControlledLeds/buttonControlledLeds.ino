/*
 * Use buttons S1, S2, and S4 to control LEDs L1-L4.
 * 
 * LEDS on pin 10 and 11(L3 & L4) and connected to button S4.
 * The S3 button is tied to the same pin as button 4
 * except on the low.
 * 
 * You need to switch the red/white switches above the LED
 * to "To Control LEDs" setting (down).
 * 
 * I still notice inconsistent behavior with the buttons.
 * Button 1 is finicky like it isn't soldered well and the
 * pressed state is not maintained perfectly.
 * 
 * Button 4 turns the LED on and off properly except
 * the LED stays on for a certain period after letting
 * go of the button. The time varies from instant to up
 * to a second.
 * 
 * 10/23/2016
 * NanoDano <nanodano@devdungeon>
 * http://www.devdungeon.com
 */
// Buttons
int inputPin1 = 9; 
int inputPin2 = 8;
int inputPin3 = A5;

// LEDs
int ledPin1 = 13; // Leftmost LED
int ledPin2 = 12;
int ledPin3 = 11;
int ledPin4 = 10; // Rightmost LED

void setup() {
  pinMode(inputPin1, INPUT);
  pinMode(inputPin2, INPUT);
  pinMode(inputPin3, INPUT);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
}

void loop() {
  digitalWrite(ledPin1, digitalRead(inputPin1));
  digitalWrite(ledPin2, digitalRead(inputPin2));
  digitalWrite(ledPin3, digitalRead(inputPin3));
  digitalWrite(ledPin4, digitalRead(inputPin3));
}
