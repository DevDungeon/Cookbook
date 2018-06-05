/*
  LCD i2c example code for tinylab
  modified 22 Jan 2016
  by Yasin Kaya (selengalp)
*/

// include the library code:
#include <Wire.h>
#include <LiquidTWI2.h>

// Connect via i2c, address 0x20 
LiquidTWI2 lcd(0x20);

void setup() {
  // set the LCD type
  lcd.setMCPType(LTI_TYPE_MCP23008); 
  
  // set up the LCD's number of rows and columns:
  lcd.begin(16, 2);
} 

void loop() {
  // turn on LCD backlight
 lcd.setBacklight(HIGH);
 
 // what will write first line
 lcd.print("    TINYLAB     ");
 
 lcd.setCursor(0, 1);
 
 // what will write second line
 lcd.print(" by Sixfab Inc.");
}
 
 


