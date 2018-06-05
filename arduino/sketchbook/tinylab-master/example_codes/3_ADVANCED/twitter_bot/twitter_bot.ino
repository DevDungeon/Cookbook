// coded by Yasin Kaya (@selengalp)
// inspired by https://www.youtube.com/channel/UCv1D6zrC0ZL0PSgM6tdEpPg/videos

// include the library code:
#include <Wire.h>
#include <LiquidTWI2.h>
#include <Time.h>
#include <DS1307RTC.h>

// definations
#define DEBUG true

#define APIKEY "xxxxxxxxxxxxxxxx" //  your thingspeak twitter api key 
#define TARGET_IP "api.thingspeak.com" // direction IP thingspeak
#define TARGET_PORT "80" // port 80
#define ID "xxxxxx"  // name of wireless access point to connect to 
#define PASS "xxxxxx"  // wifi password    

#define LM35_PIN A3
#define LDR_PIN A2                            

// Connect via i2c, address 0x20
LiquidTWI2 lcd(0x20);

boolean tweet_trigger = false;
// int hour_first_digit = 0;
// int hour_second_digit = 0;
// int minute_first_digit = 0;
// int minute_second_digit = 0;
// int recent_hour = (hour_first_digit * 10) + hour_second_digit;
// int recent_minute =  (minute_first_digit * 10) + minute_second_digit;

void setup()
{
	Serial.begin(115200); // debug serial port
  Serial1.begin(115200); // esp serial port
  
  // set the LCD type
  lcd.setMCPType(LTI_TYPE_MCP23008); 

  // set up the LCD's number of rows and columns:
  lcd.begin(16, 2);

  delay(1000); // initial delay

  sendData("AT+RST\r\n",1000,DEBUG); // reset ESP8266

    sendData("AT+CWMODE=1\r\n",1000,DEBUG); // configure ESP8266 mode 
   	
   	// connect to internet via wireless network  
    String cmd="AT+CWJAP=\"";  
    cmd+=ID;
    cmd+="\",\"";
    cmd+=PASS;
    cmd+="\"";      
	sendData( cmd+"\r\n",1000,DEBUG); 
    
    delay(1000);

    sendData("AT+CIPMUX=0\r\n",1000,DEBUG); // Configure server connection type 
    
}
 
void loop()
{ 
	tmElements_t tm;

	if (RTC.read(tm)) {
  	} else {
    	if (RTC.chipPresent()) {
      		Serial.println("The DS1307 is stopped.  Please run the SetTime");
      		Serial.println("example to initialize the time and begin running.");
      		Serial.println();
    	} else {
      		Serial.println("DS1307 read error!  Please check the circuitry.");
      		Serial.println();
      		}
    	}    
  	

	// read the temperature
	int temp = (5.0 * analogRead(LM35_PIN) * 100.0) / 1024;
	// read the light 
    int light = ((2500.0 / (analogRead(LDR_PIN) * (5.0 / 1024.0))) - 500) / 10.0;          
   	
   	// converting int to string
   	String temp_value = (String)temp;
   	String light_value = (String)light;

   	// twitter status
   	String  twitter_status = ("Tinylab reports, Temperature: " + temp_value + " °C" + "   Light : " + light_value +" lx");
   	
    if(tm.Minute == 47 && tm.Hour == 13 && !tweet_trigger){
      tweet_trigger = true;
      lcd.clear();
      lcd.print("Preparing Tweet");
    }
   	if(digitalRead(9) == false && !tweet_trigger){
   		tweet_trigger = true;
      lcd.clear();
      lcd.print("Preparing Tweet");
   	}

   	if(tweet_trigger){
	    String connection_command = "AT+CIPSTART=\"TCP\",\""; 
	    connection_command += TARGET_IP;
	    connection_command += "\",80\r\n";         



	    sendData(connection_command,1000,DEBUG);        

	    // Create HTTP POST Data             
	    String tsData = "api_key=" APIKEY "&status=" + twitter_status ;    
	     
	    String tweet_request = "POST /apps/thingtweet/1/statuses/update HTTP/1.1\n";
	    tweet_request += "Host: api.thingspeak.com\n";
	    tweet_request += "Connection: close\n";
	    tweet_request += "Content-Type: application/x-www-form-urlencoded\n";
	    tweet_request += "Content-Length: ";
	    tweet_request += tsData.length();
	    tweet_request += "\n\n";
	    tweet_request += tsData;
	       
	      
		String send_request = "AT+CIPSEND=";     
		send_request += tweet_request.length();
		send_request +="\r\n";     
		  
		sendData(send_request,1000,DEBUG);
		sendData(tweet_request,1000,DEBUG);   

		// close server connection after tweet            
		sendData("AT+CIPCLOSE=0\r\n",1500,DEBUG);
		     
		delay(2000); // thingspeak delay

    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Twitter Status");
    lcd.setCursor(0,1);
    lcd.print("     Updated");

    delay(8000); // thingspeak delay
		tweet_trigger = false; 
 	}
}
 
// send AT command function 
String sendData(String command, const int timeout, boolean debug)
{
    String response = "";
    
    Serial1.print(command); // send the read character to the esp8266
    
    long int time = millis();
    
    while( (time+timeout) > millis())
    {
      while(Serial1.available())
      {
        // The esp has data so display its output to the serial window 
        char c = Serial1.read(); // read the next character.
        response += c;
      }  
    }
    
    if(debug)
    {
      Serial.print(response);
    }
    
    return response;
}