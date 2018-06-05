// coded by yasin kaya (selengalp)

#define MOTOR_PIN 5

uint8_t motor_speed = 0;

void setup()
 {
 	Serial.begin(9600);
 	Serial1.begin(9600);

 	for(int i=10;i<13;i++){
 		pinMode(i, OUTPUT);
 	}
 } 

 void loop()
 {

 	if(Serial1.available()){
 		motor_speed = Serial1.read();

 		Serial.print(motor_speed);
 		Serial.print("\n");		
 	}

 	analogWrite(MOTOR_PIN,motor_speed);

 	if(motor_speed / 64 == 0 ){
 		if(motor_speed == 0){
 			digitalWrite(13, LOW);
	 		digitalWrite(12, LOW);
	 		digitalWrite(11, LOW);
	 		digitalWrite(10, LOW);
 		}else{
 			digitalWrite(13, HIGH);
 			digitalWrite(12, LOW);
 			digitalWrite(11, LOW);
 			digitalWrite(10, LOW);
 		}
	}else if(motor_speed / 64 == 1){
		digitalWrite(13, HIGH);
 		digitalWrite(12, HIGH);
 		digitalWrite(11, LOW);
 		digitalWrite(10, LOW);
	}else if(motor_speed / 64 == 2){
		digitalWrite(13, HIGH);
		digitalWrite(12, HIGH);
		digitalWrite(11, HIGH);
		digitalWrite(10, LOW);
	}else if(motor_speed / 64 == 3){
		digitalWrite(13, HIGH);
		digitalWrite(12, HIGH);
		digitalWrite(11, HIGH);
		digitalWrite(10, HIGH);
	}
 }