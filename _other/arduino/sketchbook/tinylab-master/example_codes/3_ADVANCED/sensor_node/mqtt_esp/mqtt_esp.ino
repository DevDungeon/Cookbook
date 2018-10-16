/*
 Basic ESP8266 MQTT example

 This sketch demonstrates the capabilities of the pubsub library in combination
 with the ESP8266 board/library.

 It connects to an MQTT server then:
  - publishes "hello world" to the topic "fromESP" every two seconds
  - subscribes to the topic "toESP", printing out any messages
    it receives. NB - it assumes the received payloads are strings not binary
  - If the first character of the topic "toESP" is an 1, switch ON the ESP Led,
    else switch it off

 It will reconnect to the server if the connection is lost using a blocking
 reconnect function. See the 'mqtt_reconnect_nonblocking' example for how to
 achieve the same result without blocking the main loop.

 To install the ESP8266 board, (using Arduino 1.6.4+):
  - Add the following 3rd party board manager under "File -> Preferences -> Additional Boards Manager URLs":
       http://arduino.esp8266.com/stable/package_esp8266com_index.json
  - Open the "Tools -> Board -> Board Manager" and click install for the ESP8266"
  - Select your ESP8266 in "Tools -> Board"

*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>

long lastMsg = 0;
char msg[75];
byte byte_read[3] = {0};
int temp_value = 0;
int light_value = 0;

const char* ssid = "xxxxxx"; // your wireless id  
const char* password = "xxxxxx"; // your wireless password
const char* mqtt_server = "broker.mqttdashboard.com"; // open source mqtt server

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);

  setup_wifi();

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);   // We start by connecting to a WiFi network
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  //Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    // Attempt to connect
    if (client.connect("ESP8266Client")) {
      // client.publish("fromESP", "hello world");    // Once connected, publish an announcement...
      client.subscribe("toESP");   // ... and resubscribe
    } else {
      delay(1000); // Wait 5 seconds before retrying
    }
  }
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  if (Serial.available()) {
    int i = 0;
    while(Serial.available() > 0){
      byte_read[i] = Serial.read();
      i++;
      delay(2);
      }
    
    temp_value = (int)byte_read[0];
    light_value = (int)( (byte_read[2] >> 8) + byte_read[1] );
    
    sprintf(msg, "Temperature: %d   Lux: %d", temp_value, light_value);
    client.publish("fromESP", msg);
  }
}

