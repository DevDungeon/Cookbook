/*
 * Send a message over serial for each button pressed (S1-S4)
 * 
 * Buttons S3 and S4 are connected to the same pin so only
 * using the fourth button.
 * 
 * Button S4 tends to "stick" on after I let go.
 * 
 * 10/23/2016
 * NanoDano <nanodano@devdungeon>
 * http://www.devdungeon.com
 */
int button1Pin = 9; 
int button2Pin = 8;
int button4Pin = A5; // High

void setup() {
  pinMode(button1Pin, INPUT);
  pinMode(button2Pin, INPUT);
  pinMode(button4Pin, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(button1Pin) == LOW) {
    Serial.write("Button 1 Low\n");
  }
  if (digitalRead(button2Pin) == LOW) {
    Serial.write("Button 2 Low\n");
  }
  if (digitalRead(button4Pin) == HIGH) {
    Serial.write("Button 4 High\n");
  }
if (digitalRead(button4Pin) == HIGH) {
    Serial.write("Button 4 High\n");
  }
}
