#ifndef ArduinoCloudThingBase_h
#define ArduinoCloudThingBase_h

#include <Arduino.h>
#include "lib/Timer.h"

// Uncomment to allow the debut output
#define CLOUD_DEBUG_STREAM Serial // SAMD
// #define CLOUD_DEBUG_STREAM SerialUSB // SAM3X Native

/// Configurations
#define SERVER_DOMAIN  "mqtt.arduino.cc"
#define SERVER_PORT 8883
#define PROPERTIES_MAX 10

/// Permission
#define R "R"
#define RW "RW"

/// Data Type
#define CHARSTRING "charstring"
#define FLOAT "float"
#define INT "int"

/// Temperature
#define TEMPERATURE_C "celsius"
#define TEMPERATURE_F "fahrenheit"

/// Distance
#define LENGTH_M "meters"
#define LENGTH_C "centimeters"
#define LENGTH_I "inches"

/// MIX
#define PERCENTAGE "percentage"
#define ANALOG "analog"
#define LUMEN "lumen"
#define PPM "ppm" // gas part per million
#define STATUS "status"

//// Polices
#define TIMED "timed"
#define ON_CHANGE "on_change"

#ifndef MQTT_BUFFER_SIZE
#define MQTT_BUFFER_SIZE 256
#endif

#define MQTTCLIENT_QOS1 0
#define MQTTCLIENT_QOS2 0

/// Status
#define STATUS_TOPIC "status"
#define ONLINE_STATUS_PAYLOAD "online"
#define OFFLINE_STATUS_PAYLOAD "offline"

class ArduinoCloudThingBase {

public:
    void addProperty(const char* name, const char* datatype, const char* permission);
    void addProperty(const char* name, const char* datatype, const char* permission, const char* policy);
    void addProperty(const char* name, const char* datatype, const char* permission, const char* policy, int lapse);
    void addExternalProperty(const char* other_device_name, const char* name, const char* datatype);

    void writeProperty(const char* name, const char* value);
    void writeProperty(const char* name, float value);
    void writeProperty(const char* name, int value);
    void writeProperty(const char* name, String value);

    String readProperty(const char* name);
    String readProperty(const char* other_device_name, const char* name);

    void enableDebug();
    void disableDebug();
    void push();

protected:
    void begin(const char* name, const char* username, const char* id, const char* password);
    void addExternalProperty(const char* other_device_name, const char* name, const char* datatype, const char* permission, const char* policy, int lapse);
    virtual void publish(const char * topic, const char* payload);

    String buildTopicProperty(int property_index);
    int discoverProperty(const char* device_name, const char* name);

    // void addProperty(const char* other_device_name, const char* name, const char* datatype, const char* permission, const char* policy, int lapse);
    void updatePropertyFromTopic(const char* topic, const char* value);

    // Object configuration
    const char* username;
    const char* id;
    const char* password;
    const char* name;

    // Property configuration
    struct property_conf {
        const char* name;
        const char* datatype;
        const char* permission;
        const char* device_name;
        const char* policy;
        String value;
        long lapse;
        long runtime;
    };

    bool cloud_debug = false;
    property_conf* properties[PROPERTIES_MAX];
    int properties_count = 0;
};
#endif
