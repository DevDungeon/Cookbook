/*

  ArduinoCloudThing ReadAndWrite

  Example that explaines the use of read and write properties and how to
  manage a property of others devices.

  Arduino Cloud -> https://cloud.arduino.cc/cloud

  IMPORTANT: This sketch requires the arduino.cc root SSL certificate loaded on your board.
             The board comes with this certificate preloaded. The procedure to change the 
             preloaded set of root certificates can be found here:
             https://www.arduino.cc/en/Tutorial/FirmwareUpdater

  created May 2016
  by Gilberto Conti and Sandeep Mistry

*/

#include <WiFi101.h>
#include <ArduinoCloud.h>


#include "arduino_secrets.h" 
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
/////// Wifi Settings ///////

char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;

// Arduino Cloud settings and credentials
const char userName[] = SECRET_USER_NAME;
const char thingName[] = SECRET_THING_NAME;
const char thingId[] = SECRET_THING_ID;
const char thingPsw[]  = SECRET_THING_PSW;

WiFiSSLClient sslClient;

// build a new object "cloudObject"
ArduinoCloudThing cloudObject;

const int ledPin = 6;

void setup() {
  Serial.begin (9600);

  // attempt to connect to WiFi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);

  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // unsuccessful, retry in 4 seconds
    Serial.print("failed ... ");
    delay(4000);
    Serial.print("retrying ... ");
  }

  // setup the "cloudObject"
  cloudObject.enableDebug(); // enable the serial debug output
  cloudObject.begin(thingName, userName, thingId, thingPsw, sslClient);

  // define the properties
  cloudObject.addProperty("bulb", STATUS , RW);
  cloudObject.addExternalProperty("lampSwitch", "position", STATUS); // this property is owned by "lampSwitch" object
}

void loop() {
  // subscribes to RW properties and look at the connections status

  cloudObject.poll();

  // read the lamp switch "position", update "bulb" property accordingly
  if (cloudObject.readProperty("lampSwitch", "position") == "on") {
    cloudObject.writeProperty("bulb", "on");
  } else {
    cloudObject.writeProperty("bulb", "off");
  }

  // read the "bulb" property, update the LED accordingly
  if (cloudObject.readProperty("bulb") == "on") {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }


  if ( WiFi.status() != WL_CONNECTED) {
    while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
      // unsuccessful, retry in 4 seconds
      Serial.print("failed ... ");
      delay(4000);
      Serial.print("retrying ... ");
    }
  }
  
  delay(1000);
}
