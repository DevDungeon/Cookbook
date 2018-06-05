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



 /* we always wait a bit between updates of the display */
 unsigned long delay_time = 1000;

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
 }

 void loop() {
  // display the characters for the word "tinylab" and "2016"
  writeTinylabOn7Segment();
}

void writeTinylabOn7Segment() {
  // display the characters for the word "tinylab" and "2016"

  lc.setRow(0, 0, B00001111);
  lc.setRow(0, 1, B00000110);
  lc.setRow(0, 2, B01110110);
  lc.setRow(0, 3, B00111011);

  delay(delay_time);
  lc.clearDisplay(0);

  lc.setRow(0, 0, B00001110);
  lc.setRow(0, 1, B01111101);
  lc.setRow(0, 2, B00011111);

  delay(delay_time);
  lc.clearDisplay(0);

  lc.setDigit(0,0,2,false);
  lc.setDigit(0,1,0,false);
  lc.setDigit(0,2,1,false);
  lc.setDigit(0,3,6,false);
  
  delay(delay_time);
  lc.clearDisplay(0);
  
}












