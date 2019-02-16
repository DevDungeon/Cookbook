// coded by Yasin Kaya (@selengalp)

//definations
#define RELAY_PIN A4

byte relay_situation = 10;

void setup()
{
	Serial1.begin(9600);
	Serial.begin(115200);
	pinMode(RELAY_PIN, OUTPUT);
}

void loop()
{
	if(Serial1.available()){
		relay_situation = Serial1.read(); 
		Serial.write(relay_situation);		
	}

	if(relay_situation == 0){
		digitalWrite(RELAY_PIN, LOW);
		Serial.print("Lamp Off");
		delay(10);
	}
	if(relay_situation == 255){
		digitalWrite(RELAY_PIN, HIGH);
		Serial.print("Lamp On");
		delay(10);
	}   
}