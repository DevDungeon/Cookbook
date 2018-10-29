//coded by yasin kaya (selengalp)

#define LM35_PIN A3
#define LDR_PIN A2

void setup()
{
	Serial1.begin(115200);
	Serial.begin(9600);
}

byte temp = 0;
int light = 0;


void loop()
{
	temp = (5.0 * analogRead(LM35_PIN) * 100.0) / 1024;
	light = ((2500.0 / (analogRead(LDR_PIN) * (5.0 / 1024.0))) - 500) / 10.0;

	byte light_high = light << 8;
	byte light_low = light - (light_high >> 8);
	Serial1.write(temp);
	Serial1.write(light_low);
	Serial1.write(light_high);
	

	Serial.print(temp);
	Serial.print("\t");
	Serial.print(light);
	Serial.print("\n");
	delay(3000);
}
