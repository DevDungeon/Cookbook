#include <ArduinoCloudThing.h>

ArduinoCloudThing::ArduinoCloudThing() {
}

void ArduinoCloudThing::begin(const char* name, const char* username, const char* id, const char* password, Client &client) {
    ArduinoCloudThingBase::begin(name, username, id, password);

    this->client = new MQTT::Client<ArduinoCloudThing, Network, Timer, MQTT_BUFFER_SIZE, 0>(network);
    this->network.setClient(&client);
    this->options = MQTTPacket_connectData_initializer;
    this->client->defaultMessageHandler.attach<ArduinoCloudThing>(this, &ArduinoCloudThing::callback);
}

boolean ArduinoCloudThing::connect() {
    if(!network.connect((char*)SERVER_DOMAIN, SERVER_PORT)) {
        return false;
    }

    char statusTopic[strlen(username) + strlen(name) + strlen(STATUS_TOPIC) + 3]; // 2 extra bytes for /'s, 1 for null terminator
    sprintf(statusTopic, "%s/%s/%s", username, name, STATUS_TOPIC);
    //  if (cloud_debug) {
    //      CLOUD_DEBUG_STREAM.print("Will Topic: ");
    //      CLOUD_DEBUG_STREAM.println(statusTopic);
    //  }
    options.clientID.cstring = (char*)name;
    options.username.cstring = (char*)id;
    options.password.cstring = (char*)password;
    options.keepAliveInterval = 10;
    options.willFlag = 0x1;
    options.will.topicName.cstring = (char*)statusTopic;
    options.will.message.cstring = (char*)OFFLINE_STATUS_PAYLOAD;
    options.will.retained = 0x1;

    if (client->connect(options) == 0) {
        publish(statusTopic, (char*)ONLINE_STATUS_PAYLOAD, strlen(ONLINE_STATUS_PAYLOAD), true);
        return true;
    }

    return false;
}

void ArduinoCloudThing::publish(const char * topic, const char * payload) {
  publish(topic, (char*)payload, (unsigned int)strlen(payload));
}

void ArduinoCloudThing::publish(const char * topic, const char * payload, unsigned int length, bool retained) {
    MQTT::Message message;
    message.qos = MQTT::QOS0;
    message.retained = retained;
    message.dup = false;
    message.payload = (void*)payload;
    message.payloadlen = length;
    client->publish(topic, message);
}

// Reconnect to the mqtt broker
void ArduinoCloudThing::poll() {
    if (!client->isConnected()){
        if (cloud_debug) {
            CLOUD_DEBUG_STREAM.println("Connecting to mqtt broker...");
        }
        if (!connect()){
            return;
        }
        if (cloud_debug) {
            CLOUD_DEBUG_STREAM.println("Connected");
        }
        mqttSubscribe();
    }
    if(!network.connected() && client->isConnected()) {
      client->disconnect();
    }
    client->yield();
}

// Subscribe to all proprie that have RW permission
void ArduinoCloudThing::mqttSubscribe(){
    for (int i=0; i<properties_count; i++){
        if (strcmp(properties[i]->permission, "RW") == 0) {
            String topic = buildTopicProperty(i);
            if (cloud_debug) {
            CLOUD_DEBUG_STREAM.print("Subscribe to: ");
            CLOUD_DEBUG_STREAM.println(topic);
            }
            client->subscribe(topic.c_str(), MQTT::QOS0, NULL);
        }
    }
}

ArduinoCloudThing ArduinoCloudThing::callback(MQTT::MessageData& messageData) {
    MQTT::Message &message = messageData.message;
    // null terminate topic to create String object
    int len = messageData.topicName.lenstring.len;
    char topic[len+1];
    memcpy(topic, messageData.topicName.lenstring.data, (size_t)len);
    topic[len] = '\0';

    char * payload = (char *)message.payload;
    payload[message.payloadlen] = '\0';

    updatePropertyFromTopic(topic, payload);

    return *this;
}
