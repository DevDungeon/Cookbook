#ifndef ArduinoCloudThing_h
#define ArduinoCloudThing_h

#include <ArduinoCloudThingBase.h>
#include <Client.h>
#include <Stream.h>
#include "lib/mqtt/MQTTClient.h"
#include "lib/Network.h"

#ifndef MQTT_BUFFER_SIZE
#define MQTT_BUFFER_SIZE 256
#endif

#define MQTTCLIENT_QOS1 0
#define MQTTCLIENT_QOS2 0

class ArduinoCloudThing : public ArduinoCloudThingBase {
public:
    ArduinoCloudThing();
    void begin(const char* name, const char* username, const char* id, const char* password, Client &client);
    void poll();

protected:
    virtual void publish(const char * topic, const char* payload);

private:
    ArduinoCloudThing callback(MQTT::MessageData& messageData);
    void mqttSubscribe();
    boolean connect();
    void publish(const char * topic, const char * payload, unsigned int length, bool retained = false);

    Network network;
    MQTT::Client<ArduinoCloudThing, Network, Timer, MQTT_BUFFER_SIZE, 0> * client;
    MQTTPacket_connectData options;
};

#endif
