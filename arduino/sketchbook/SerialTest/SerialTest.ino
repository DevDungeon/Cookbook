

void setup()
{
  // start serial port at 9600 bps and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }


}

void loop()
{
  char inByte;
  if (Serial.available() > 0) {
    inByte = Serial.read();
    Serial.print(inByte);
  } else {
//    Serial.println("No serial data available.");
  }
}
