
uint8_t incoming_data;
boolean tx_ok = false;

void setup()
{
	Serial.begin(115200);
	Serial1.begin(9600);
}

void loop()
{
	// if(Serial1.available()){
	// 	incoming_data = Serial1.read();
	// 	Serial.print(incoming_data);
	// 	tx_ok = true;
	// 	delay(20);	
	// }

	// if(tx_ok == true){
	// 	if(incoming_data == 255){
	// 		Serial1.write(155);
	// 	}
	// 	tx_ok = false;
	// }

	Serial1.write(255);
	delay(50);
}