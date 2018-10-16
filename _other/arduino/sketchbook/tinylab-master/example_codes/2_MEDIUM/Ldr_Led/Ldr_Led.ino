/*
 * Turn on or turn off the LED with photoresistor
 * for tinylab
 * 
 * created 22 Jan 2016
 * by Yasin Kaya (selengalp) 
 */
 *\

// set the LED pin
int led_pin = 13;

// set the photoresistor pin
int ldr_pin = A2;
// variable of ldr raw value 
int ldr_raw_value = 0;

void setup() {
  // setup pin direction		
  pinMode(led_pin,OUTPUT);
}

void loop() {
	// reading ldr raw value
	ldr_raw_value = analogRead(ldr_pin);

	// if raw value is greater than 500, led is on, else led is off  
	if(ldr_raw_value > 500){
		digitalWrite(led_pin,HIGH);
		}else{
			digitalWrite(led_pin,LOW);
		}
	}
