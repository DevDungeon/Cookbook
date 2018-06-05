/*
 * Thermometer for tinylab
 * created 22 Jan 2016
 * by Okan Saraçoğlu
 */


int temp_c = 0;
int temp_f = 0;

// set the LM35 temperature sensor pin A3
int LM35_PIN = A3;

// include the library code:
#include <Wire.h>
#include <LiquidTWI2.h>

// Connect via i2c, address 0x20 
LiquidTWI2 lcd(0x20);

void setup() {
  Serial.begin(9600);
  // set the LCD type
  lcd.setMCPType(LTI_TYPE_MCP23008);

  lcd.begin(16, 2);
  
}

void loop() {
  // turn on the LCD backlight
  lcd.setBacklight(HIGH);

  // moving lcd cursor 
  lcd.setCursor(6, 0);

  // reading lm35 temperature sensor and calculating temperature using raw value
  // temperature as celcius
  temp_c = (5.0 * analogRead(LM35_PIN) * 100.0) / 1024;
  // temperature as fahrenheit
  temp_f = ((temp_c * 9) / 5) + 32;

  // show the temperature with centigrade first line 
  lcd.setCursor(6, 0);
  lcd.print(temp_c, 1);
  lcd.setCursor(8, 0);
  lcd.print((char)223);
  lcd.print("C");
  
 // show the temperature with fahrenheit second line 
  lcd.setCursor(6, 1);
  lcd.print(temp_f, 1);
  lcd.setCursor(8, 1);
  lcd.print((char)223);
  lcd.print("F");

  delay(1000);
}

