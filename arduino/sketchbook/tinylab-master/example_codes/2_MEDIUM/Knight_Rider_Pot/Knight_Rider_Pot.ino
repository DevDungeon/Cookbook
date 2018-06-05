/* Knight Rider for tinylab

* @author: David Cuartielles
modified 22 Jan 2016
by Yasin Kaya
*/

int pin_array[] = {13, 12, 11, 10};
int count = 0;
int timer = 30;
int pot_pin = A0;
int pot_value = 0;

void setup(){

  // setup pin directions  
  for (count=0;count<4;count++) {
    pinMode(pin_array[count], OUTPUT);
  }
  
}

void loop() {

  // reading potentiometer value
  pot_value = analogRead(pot_pin);
  
  // configurating delay time according to pot. value
  timer = 100 - pot_value / 10.23;

  // knight rider codes
  for (count=0;count<3;count++) {
   digitalWrite(pin_array[count], HIGH);
   delay(timer);
   digitalWrite(pin_array[count + 1], HIGH);
   delay(timer);
   digitalWrite(pin_array[count], LOW);
   delay(timer*2);
 }
 for (count=3;count>0;count--) {
   digitalWrite(pin_array[count], HIGH);
   delay(timer);
   digitalWrite(pin_array[count - 1], HIGH);
   delay(timer);
   digitalWrite(pin_array[count], LOW);
   delay(timer*2);
 }
}



