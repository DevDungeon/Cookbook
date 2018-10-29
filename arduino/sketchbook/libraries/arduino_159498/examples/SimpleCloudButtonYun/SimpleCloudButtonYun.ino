/*

  ArduinoCloudThing Cloud Button

  Simple cloud button example that use the BridgeSSL client and display on the
  arduino cloud dashboard the value of button.

  Arduino Cloud -> https://cloud.arduino.cc/cloud

  IMPORTANT: in order to establish the TLS connection and use the BridgeSSL
  the Yun firmware version should be >=1.6.2, look at
  https://www.arduino.cc/en/Tutorial/YunSysupgrade

  created May 2016
  by Gilberto Conti and Sandeep Mistry

*/

#include <ArduinoCloud.h>
#include <BridgeSSLClient.h>
#include "arduino_secrets.h" 
BridgeSSLClient sslClient;

// build a new thing "cloudObject"
ArduinoCloudThing cloudObject;


///////please enter your sensitive data in the Secret tab/arduino_secrets.h
// Arduino Cloud settings and credentials
const char userName[] = SECRET_USER_NAME;
const char thingName[] = SECRET_THING_NAME;
const char thingId[] = SECRET_THING_ID;
const char thingPsw[]  = SECRET_THING_PSW;
const int buttonPin = 6;

void setup() {
  SerialUSB.begin(9600);

  // configure the button pin as input
  pinMode(buttonPin, INPUT);

  // start the bridge
  Bridge.begin();

  // setup the "cloudObject"
  cloudObject.enableDebug(); // eneble the serial debug output
  cloudObject.begin(thingName, userName, thingId, thingPsw, sslClient);

  // define the properties
  cloudObject.addProperty("position", STATUS , R);
}

void loop() {
  // subscribes to RW properties and look at the connections status
  cloudObject.poll();

  // read the button
  if (digitalRead(buttonPin) == HIGH) {
    // button is pressed, write position as "on"
    cloudObject.writeProperty("position", "on");
  } else {
    // button is released, write position as "off"
    cloudObject.writeProperty("position", "off");
  }

  delay(1000);

  if ( WiFi.status() != WL_CONNECTED) {
    while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
      // unsuccessful, retry in 4 seconds
      Serial.print("failed ... ");
      delay(4000);
      Serial.print("retrying ... ");
    }
  }
}
