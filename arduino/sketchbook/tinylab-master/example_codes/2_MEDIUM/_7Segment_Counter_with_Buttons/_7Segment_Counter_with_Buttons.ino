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

 int up_button=8;
 int down_button=9;
 int num1=0;
 int num2=0;
 int num3=0;
 int num4=0;



 /* we always wait a bit between updates of the display */
 unsigned long delay_time = 10;

void setup() {
  Serial.begin(9600);
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
  pinMode(9,INPUT);
}



void loop() {
  if(digitalRead(up_button)==LOW){
    lc.clearDisplay(0);
    
    // units digit
    num1++;
    if(num1>9){
     num1=0;
     num2++;
   }
    // tents digit
    if(num2>9){
     num2=0;
     num3++;
   }
    // hundreds and thousends digits
    if(num3>9){
     num3=0;
     num4++;
   }

   }else if(digitalRead(down_button)==LOW){
     Serial.println(digitalRead(down_button));
     lc.clearDisplay(0);

       // units digit
       num1--;
       if(num1<0){
        num1=9;
        num2--;
      }
       // tents digit
       if(num2<0){
        num2=9;
        num3--;
      }
       // hundreds and thousends digits
       if(num3<0){
        num3=9;
        num4--;

      }
    }

  // set digits with nums 
  lc.setDigit(0, 0, num4, false);
  lc.setDigit(0, 1, num3, false);
  lc.setDigit(0, 2, num2, false);
  lc.setDigit(0, 3, num1, false);
  delay(delay_time);
}













