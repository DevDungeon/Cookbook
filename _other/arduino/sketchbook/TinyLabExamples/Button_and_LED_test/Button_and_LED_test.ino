/*
 * Test the first two LED and buttons on TinyLab S1, S2, L1, L2
 * Make sure the jumpers are set so these pins are not using the
 * on-board Arduino but routed to the tinylab inputs.
 */
const int button1Pin = 9; // S1
const int button2Pin = 8; // S2

const int button34Pin = A5; // S3  & S4

const int led1Pin = 13; // L1
const int led2Pin = 12; // L2
const int led3Pin = 11; // L3
const int led4Pin = 10; // L4

int button1State = 0;
int button2State = 0;
int button34State = 0;

void setup() {
  pinMode(led1Pin, OUTPUT);
  pinMode(led2Pin, OUTPUT);
  pinMode(led3Pin, OUTPUT);
  pinMode(led4Pin, OUTPUT);
  pinMode(button1Pin, INPUT);
  pinMode(button2Pin, INPUT);
  pinMode(button34Pin, INPUT);
}
//
//    if(analogRead(S3_PIN) > 100 && analogRead(S3_PIN) < 300){
//        S3_clicked = true;
//        digitalWrite(L3_PIN,HIGH);
//      }else{
//        S3_clicked = false;
//        digitalWrite(L3_PIN,LOW);
//      }

void loop() {
  button1State = digitalRead(button1Pin);
  button2State = digitalRead(button2Pin);
  button34State = digitalRead(button34Pin);

  if (button1State == LOW) { // Buttons high by default
    digitalWrite(led1Pin, HIGH);
  } else {
    digitalWrite(led1Pin, LOW);
  }
  if (button2State == LOW) {
    digitalWrite(led2Pin, HIGH);
  } else {
    digitalWrite(led2Pin, LOW);
  }
  if (button34State == HIGH) { // default state
    digitalWrite(led3Pin, HIGH);
    digitalWrite(led4Pin, LOW);
  } else { // button34State is LOW (pressed)
    digitalWrite(led3Pin, LOW);
    digitalWrite(led4Pin, HIGH);
  }
}

