/*
 source of library: https://github.com/wayoda/LedControl
 created by Okan Saraçoğlu

 */

 #include "LedControl.h"

/*
 Now we need a LedControl to work with.
 pin 10 is connected to the DataIn
 pin 12 is connected to the CLK
 pin 11 is connected to LOAD
 We have only a single MAX72XX.
 */
 LedControl lc = LedControl(10, 12, 11, 1);
 int dice=0;
 int button_pin=8;

 void setup() {
  /*
   The MAX72XX is in power-saving mode on startup,
   we have to do a wakeup call
   */
   lc.shutdown(0, false);
   /* Set the brightness to a medium values */
   lc.setIntensity(0, 8);
   /* and clear the display */
   lc.clearDisplay(0);
   pinMode(8,INPUT);
 }



 void loop() {
   if(digitalRead(button_pin)==LOW){
    randomSeed(analogRead(A0));
    dice=random(1,7);

    for(int i=0;i<250;i=i+50){
     dice=random(1,7);
     showNumber(dice);
     delay(i);
     dice=random(1,7);
     showNumber(dice);
     delay(i);
     dice=random(1,7);
     showNumber(dice);
     delay(i);
     dice=random(1,7);
     showNumber(dice);
     delay(i);
     dice=random(1,7);
     showNumber(dice);
     delay(i);
     dice=random(1,7);
     showNumber(dice);
     delay(i);
     dice=random(1,7);
     showNumber(dice);
     delay(i);
   }
   showNumber(dice);
 }
}

void showNumber(int a) {
  lc.clearDisplay(0);
  lc.setDigit(0, 3, a, false);
}












