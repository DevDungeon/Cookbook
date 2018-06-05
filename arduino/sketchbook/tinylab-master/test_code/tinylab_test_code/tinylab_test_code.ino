
/* tinylab testing code
 * coded by Yasin Kaya (selengalp)
 * 18/05/2016		
*/

// definitions
#define S1_PIN 9
#define S2_PIN 8
#define S3_PIN A5 // LOW
#define S4_PIN A5 // HIGH
#define L1_PIN 13
#define L2_PIN 12
#define L3_PIN 11 
#define L4_PIN 10 
#define MOTOR_PIN 5
#define POT_PIN A0
#define LDR_PIN A2
#define LM35_PIN A3
#define BUZZER_PIN A1
#define SD_CS_PIN 4
#define RELAY_PIN A4
#define ROTARY_BUTTON A5 

// libraries
#include "Wire.h"
#include <Time.h>
#include <TimeLib.h>
#include <LiquidTWI2.h>
#include <RotaryEncoder.h>
#include <DS1307RTC.h>
#include <SdFat.h>
#include "LedControl.h"
#include <extEEPROM.h>
// Radio
#include <SPI.h>
#include <RF24.h>

// instances
LiquidTWI2 lcd(0x20);
RotaryEncoder encoder(6, 7);
tmElements_t tm;
SdFat SD;
LedControl lc=LedControl(10,12,11,1);
RF24 radio(8,9);

//variables
uint8_t test_selector = 0; // begin test statement
boolean c_leds = 0;
boolean c_buzz = 0;
boolean c_7seg = 0;
boolean c_sd = 0;
boolean c_eeprom = 0;
boolean c_esp = 0;
boolean c_xbee = 0;
uint8_t c_nrf = 0;
boolean c_nrf_setup = 0;
boolean c_relay = 0;
uint16_t timer = 0;
uint16_t tap_lenght = 0;
uint8_t data_xbee = 0;


boolean S1_clicked = false;
boolean S2_clicked = false;
boolean S3_clicked = false;
boolean S4_clicked = false;
int8_t rotary_pos = 0;
uint16_t pot_value = 0;
uint16_t ldr_value = 0;
int16_t lm35_value = 0;
uint16_t notes[] = {262,294,330,349,392,440,494,523};
uint16_t delay_7segment = 250;

// NRF
/***      Set this radio as radio number 0 or 1         ***/
bool radioNumber = 1;
/**********************************************************/
byte addresses[][6] = {"1Node","2Node"};
// Used to control whether this node is sending or receiving
bool role = 1;


void setup()
{
	Serial.begin(115200);
	Serial1.begin(115200);
	// LCD setup
	lcd.setMCPType(LTI_TYPE_MCP23008);
	lcd.begin(16, 2);
	lcd.setBacklight(HIGH);
	// LED
	pinMode(L1_PIN, OUTPUT);
	pinMode(L2_PIN, OUTPUT);
	pinMode(L3_PIN, OUTPUT);
	pinMode(L4_PIN, OUTPUT);
	// BUTTON
	pinMode(S1_PIN, INPUT);
	pinMode(S2_PIN, INPUT);
	pinMode(S3_PIN, INPUT);
	// RELAY
	pinMode(RELAY_PIN,OUTPUT);
	// SENSORS
	pinMode(POT_PIN, INPUT);
	pinMode(LDR_PIN, INPUT);
	pinMode(LM35_PIN, INPUT);
	// BUZZER
	pinMode(BUZZER_PIN, OUTPUT);
	// SD
	pinMode(SD_CS_PIN, OUTPUT);

	// RTC
	bool parse=false;
  bool config=false;

 	// get the date and time the compiler was run
  	if (getTime(__TIME__)) {
    parse = true;
    // and configure the RTC with this info
    if (RTC.write(tm)) {
      config = true;
    	}
  	}

  	// 7 Segment
  	/*
   	The MAX72XX is in power-saving mode on startup,
   	we have to do a wakeup call
   	*/
  	lc.shutdown(0,false);
  	/* Set the brightness to a medium values */
  	lc.setIntensity(0,8);
  	/* and clear the display */
  	lc.clearDisplay(0);
}

void loop()
{
	S1_clicked = !digitalRead(S1_PIN);	

	if(S1_clicked == false){

		if(tap_lenght < 1000 && tap_lenght > 0){
			Serial.println("click");
			test_selector++;
			tap_lenght = 0;
		}else if (tap_lenght > 1000){
			Serial.println("long click");
			test_selector = 100;
			tap_lenght =0;	
		}else{

		}

		timer = millis();
	}

	if(S1_clicked == true){
		tap_lenght = millis() - timer;		
	}

	
	// if(S1_clicked == true){
	// 	test_selector++;
	// 	delay(500);
	// }

	switch (test_selector) {

		case 4:{
	    	// motor OFF 
	    	digitalWrite(MOTOR_PIN,LOW);

	    	// Rotary Encoder Test
			encoder.tick();

	  		int8_t new_pos = encoder.getPosition();
	  		if (rotary_pos != new_pos){
			    rotary_pos = new_pos;
			}

			if(analogRead(ROTARY_BUTTON)>50){
				digitalWrite(L4_PIN, HIGH);
			}else{
				digitalWrite(L4_PIN, LOW);
			} 

			// log
			lcd.setCursor(0, 0);
			lcd.print("Rotary Position:");
			lcd.setCursor(0, 1);
			lcd.print(-1*rotary_pos);
			lcd.print("                ");
	    	break;
	    }

	    case 0:{

	    	// leds OFF
			digitalWrite(L1_PIN, LOW);
			digitalWrite(L2_PIN, LOW);
			digitalWrite(L3_PIN, LOW);
			digitalWrite(L4_PIN, LOW);

	    	lcd.setCursor(0, 0);
			lcd.print("LCD -> OK       ");
			lcd.setCursor(0, 1);
			lcd.print("           -> S1");
	    	break;
	    }
	      
	    case 1:{
	    	// LEDs Test
	    	if(c_leds == 0){

	    	// log
			lcd.setCursor(0, 0);
			lcd.print("LEDs Test       ");
			lcd.setCursor(0, 1);
			lcd.print("           -> S1");

	    	// leds ON
			digitalWrite(L1_PIN, HIGH);
			digitalWrite(L2_PIN, HIGH);
			digitalWrite(L3_PIN, HIGH);
			digitalWrite(L4_PIN, HIGH);
			
			delay(1000);

			// leds OFF
			digitalWrite(L1_PIN, LOW);
			digitalWrite(L2_PIN, LOW);
			digitalWrite(L3_PIN, LOW);
			digitalWrite(L4_PIN, LOW);			
	    	c_leds++;
	    	}	
	    break;	
	    }

	    case 2:{
	    	//Serial.println(digitalRead(S2_PIN));
	    	// Button Test
			S2_clicked = !digitalRead(S2_PIN);
			

			if(S2_clicked == true){
				digitalWrite(L2_PIN,HIGH);

				}else{
					digitalWrite(L2_PIN,LOW);
				}
			
			if(analogRead(S3_PIN) > 100 && analogRead(S3_PIN) < 300){
				S3_clicked = true;
				digitalWrite(L3_PIN,HIGH);
			}else{
				S3_clicked = false;
				digitalWrite(L3_PIN,LOW);
			}

			if(analogRead(S4_PIN) > 450 && analogRead(S4_PIN) < 550){
				S4_clicked = true;
				digitalWrite(L4_PIN,HIGH);
			}else{
				S4_clicked =false;
				digitalWrite(L4_PIN,LOW);
			}
			
			// log
			lcd.setCursor(0, 0);
			lcd.print("Button S2 S3 S4:");
			lcd.setCursor(0, 1);
			lcd.print("           -> S1");
	    	break;
	    }

	    case 3:{

	    	// motor test
	    	// motor on
			digitalWrite(MOTOR_PIN,HIGH);

			//log
			lcd.setCursor(0, 0);
			lcd.print("Motor  Test:    ");
			lcd.setCursor(0, 1);
			lcd.print("Connect a Motor!");
	    	break;
	    }


	    case 5:{
	    	// Potantiometer Test
	    	pot_value = analogRead(POT_PIN);

			// log
			lcd.setCursor(0, 0);
			lcd.print("Pot Value:      ");
			lcd.setCursor(0, 1);
			lcd.print(pot_value);
			lcd.print("                ");
	    	break;
	    }

	    case 6:{
	    	// LDR Test
	    	ldr_value = ((2500.0 / (analogRead(LDR_PIN) * (5.0 / 1024.0))) - 500) / 10.0;;

			// log
			lcd.setCursor(0, 0);
			lcd.print("Light(Lumen):   ");
			lcd.setCursor(0, 1);
			lcd.print(ldr_value);
			lcd.print("                ");
	    	break;
	    }

	    case 7:{
	    	// LM35 Test
	    	lm35_value = (5.0 * analogRead(LM35_PIN) * 100.0) / 1024;

			// log
			lcd.setCursor(0, 0);
			lcd.print("Temperature(C): ");
			lcd.setCursor(0, 1);
			lcd.print(lm35_value);
			lcd.print("                ");
	    	break;
	    }

	    case 8:{
	    	
	    	// Buzzer Test
	    	if(c_buzz == 0){

	    		// log
				lcd.setCursor(0, 0);
				lcd.print("Buzzer Test:    ");
				lcd.setCursor(0, 1);
				lcd.print("           -> S1");

	    		tone(BUZZER_PIN, 440);
	    		delay(500);
	    		// buzzer off
	    		noTone(BUZZER_PIN);
	    		c_buzz++;
	    	}
	    	break;
	    }

	    case 9:{

	    	// Relay Test

	    	// log
			lcd.setCursor(0, 0);
			lcd.print("Relay Test:     ");
			lcd.setCursor(0, 1);
			lcd.print("           -> S1");
	    	
	    	if(c_relay == 0){
	    		digitalWrite(RELAY_PIN, HIGH);
	    		delay(500);
	    		// Relay Off
	    		digitalWrite(RELAY_PIN, LOW);
	    		c_relay++;
	    	}	
	    	break;
	    }

	    case 10:{
			
			// log
			lcd.setCursor(0, 0);
			lcd.print("RTC Test:       ");
		
	    	// RTC Test
	    	if(RTC.read(tm)){

	    		lcd.setCursor(0, 1);
				lcd.print(tm.Hour);
				lcd.print("-");
				lcd.print(tm.Minute);
				lcd.print("-");
				lcd.print(tm.Second);
				lcd.print("   ");
	    	}
	    	break;
	    }

	    case 11:{
	    	// SD Test
	    	if(c_sd == 0){
	    		// log
				lcd.setCursor(0, 0);
				lcd.print("SD Card Test:   ");
				lcd.setCursor(0, 1);
				lcd.print("                ");
				
	    		if (!SD.begin(SD_CS_PIN)) {
    				lcd.setCursor(0, 1);
					lcd.print("FAILED           ");
  
		  		}else{
		   			lcd.setCursor(0, 1);
					lcd.print("SD OK           "); 
		  		}
		  		c_sd++;
	    	}
	    	break;
	    }

	    case 12:{
	    	// sd card off
	    	digitalWrite(SD_CS_PIN, HIGH);

	    	// log
			lcd.setCursor(0, 0);
			lcd.print("7 Segment Test: "); 
			lcd.setCursor(0, 1);
			lcd.print("           -> S1"); 

	    	// 7 Segment Test
	    	if(c_7seg == 0){
	    		scrollDigits();
	    		// leds OFF
				digitalWrite(L1_PIN, LOW);
				digitalWrite(L2_PIN, LOW);
				digitalWrite(L3_PIN, LOW);
				digitalWrite(L4_PIN, LOW);
	    		c_7seg++;
	    	}
	    	break;
	    }

	    case 13:{
	    	
	    	// Ext. EEPROM Test
	    	if(c_eeprom == 0){

	    		// log
				lcd.setCursor(0, 0);
				lcd.print("EEPROM Test:    ");
				lcd.setCursor(0, 1);
				lcd.print("                ");

		    	extEEPROM eep(kbits_256, 2, 64);
		    	uint8_t eepStatus = eep.begin(extEEPROM::twiClock400kHz);

		    	if(eepStatus == 0){
		    		lcd.setCursor(0, 1);
					lcd.print("OK");
					lcd.print("                    ");	
		    	}else{
		    		lcd.setCursor(0, 1);
					lcd.print("FAILED");
					lcd.print("                    ");
		    	}
	    		c_eeprom++;
	    	}
	    	break;
	    }

	    case 14:{
	    	Serial1.end();
	    	Serial1.begin(115200);
	    	delay(10);
	    	// ESP8266 Test
	    	if(c_esp == 0){

	    		// log
				lcd.setCursor(0, 0);
				lcd.print("ESP8266 Test:   "); 
		    	lcd.setCursor(0, 1);
				lcd.print("                ");

	    		Serial1.flush();
	    		lcd.setCursor(0, 1);
				lcd.print("                    ");

	    		String r = sendData("AT\r\n",1000,1);
	    		
	    		if(r == "OK")
	    		{
	    			lcd.setCursor(0, 1);
	    			lcd.print("OK");
					lcd.print("                   ");
	    			
	    		}else{
	    			lcd.setCursor(0, 1);
	    			lcd.print("FAILED");
					lcd.print("                    ");	
	    		}
	    		
	    		
	    		c_esp++;
	    	}
	    	break;
	    }

	    case 100:{
	    	boolean rx_ok = false;

	    	// Xbee Test
	    	if(c_xbee < 5){
	    		Serial1.end();
	    		delay(20);
	    		Serial1.begin(9600);
	    		// log
				lcd.setCursor(0, 0);
				lcd.print("Xbee Test:      ");
				lcd.setCursor(0, 1);
				lcd.print("                ");
				
				if(Serial1.available()){
					data_xbee = Serial1.read();
					Serial.print(data_xbee);
				}
	    		if(data_xbee == 255){
	    			lcd.setCursor(0, 1);
	    			lcd.print("OK");
					  lcd.print("                    ");
					  c_xbee = 6;	
	    		}else{
	    			lcd.setCursor(0, 1);
	    			lcd.print("FAILED");
					  lcd.print("                    ");
	    		}
	    		c_xbee++;
	    	}
	    	break;	
	    }

	    case 15:{
	    	digitalWrite(SD_CS_PIN, HIGH);

	    	if(c_nrf_setup == 0){
	    		// NRF
  				radio.begin(); 

				// Set the PA Level low to prevent power supply related issues since this is a
				// getting_started sketch, and the likelihood of close proximity of the devices. RF24_PA_MAX is default.
			    radio.setPALevel(RF24_PA_LOW);

			    // Open a writing and reading pipe on each radio, with opposite addresses
			  	if(radioNumber){
			    	radio.openWritingPipe(addresses[1]);
			    	radio.openReadingPipe(1,addresses[0]);
			 	}else{
			    	radio.openWritingPipe(addresses[0]);
			    	radio.openReadingPipe(1,addresses[1]);
			  	}
	    		c_nrf_setup++;	
	    	}	
	    	
	    	if(c_nrf < 5){
	    		// log
				lcd.setCursor(0, 0);
				lcd.print("NRF Test:       ");
	    		lcd.setCursor(0, 1);
				lcd.print("                ");
	    		
	    		unsigned long got_data = 0;
	    		/****************** Ping Out Role ***************************/  
				if (role == 1)  {
    				unsigned long data_ok = 1071; 
    				radio.stopListening();                                    // First, stop listening so we can talk.
    				Serial.println(F("Now sending"));

    				unsigned long start_time = micros();                             // Take the time, and send it.  This will block until complete
    				
    				if (!radio.write( &data_ok, sizeof(unsigned long) )){
      					Serial.println(F("failed"));
    				}
        
				    radio.startListening();                                    // Now, continue listening
				    
				    unsigned long started_waiting_at = micros();               // Set up a timeout period, get the current microseconds
				    boolean timeout = false;                                   // Set up a variable to indicate if a response was received or not
				    
				    while ( ! radio.available() ){                             // While nothing is received
				    	if (micros() - started_waiting_at > 200000 ){            // If waited longer than 200ms, indicate timeout and exit while loop
				          timeout = true;
				          break;
				        }      
				    }
				        
				    if ( timeout ){                                             // Describe the results
				    	Serial.println(F("Failed, response timed out."));
				    }else{                              
				        radio.read( &got_data, sizeof(unsigned long) );
				    }
				    delay(50);
				}

			  	if(got_data == 1071){
			  		c_nrf = 5;
			  		lcd.setCursor(0, 1);
	    			lcd.print("OK");
					lcd.print("                    ");
			  	}
			  	if (got_data != 1071 && c_nrf == 4){
				  	lcd.setCursor(0, 1);
	    			lcd.print("FAILED");
					lcd.print("                    ");  	
				}
			    c_nrf++;   
	    	}
	    	
	    	break;
	    }

	    case 16:{
	    	// log
			lcd.setCursor(0, 0);
			lcd.print("Bluetooth Test");
			lcd.print("      "); 
    		lcd.setCursor(0, 1);
			lcd.print("Put On HC-06");
			break;
	    }

	    case 17:{
	    	// log
			lcd.setCursor(0, 0);
			lcd.print("S1 Long Click!  ");
    		lcd.setCursor(0, 1);
			lcd.print("for Xbee Test!  ");
			break;
	    }
	    
	    case 101:{
	    	// log
			lcd.setCursor(0, 0);
			lcd.print("TEST COMPLETED!");
			lcd.print("      "); 
    		lcd.setCursor(0, 1);
			lcd.print("CONGRATULATIONS!");
			break;
	    }

	    case 102:{
  	    test_selector = 0;
  	    c_leds = 0;
  			c_buzz = 0;
  			c_7seg = 0;
  			c_sd = 0;
  			c_eeprom = 0;
  			c_esp = 0;
  			c_xbee = 0;
  			c_nrf = 0;
  			c_nrf_setup = 0;
  			c_relay = 0;
	    	break;
	    }
    }  
}


// FUNCTIONS 
bool getTime(const char *str){
  int Hour, Min, Sec;

  if (sscanf(str, "%d:%d:%d", &Hour, &Min, &Sec) != 3) return false;
  tm.Hour = Hour;
  tm.Minute = Min;
  tm.Second = Sec;
  return true;
}

void scrollDigits() {
  for(int i=0;i<5;i++) {
    lc.setDigit(0,3,i,false);
    lc.setDigit(0,2,i+1,false);
    lc.setDigit(0,1,i+2,false);
    lc.setDigit(0,0,i+3,false);
    delay(delay_7segment);
  }
  lc.clearDisplay(0);
  delay(delay_7segment);
}

// send AT command function 
String sendData(String command, const int timeout, boolean debug)
{
    String response = "";
    String ok = "";
    
    Serial1.print(command); // send the read character to the esp8266
    
    long int time = millis();
    
    while( (time+timeout) > millis())
    {
      while(Serial1.available())
      {
        // The esp has data so display its output to the serial window 
        char c = Serial1.read(); // read the next character.
        response += c;
        if(c == 'O'){
        	ok+=c;
        }
        if(c =='K'){
        	ok+=c;
        }
      }  
    }
    
    if(debug)
    {
      Serial.print(response);
    }
    
    return ok;
}
