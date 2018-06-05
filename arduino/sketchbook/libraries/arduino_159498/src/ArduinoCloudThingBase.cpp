#include "ArduinoCloudThingBase.h"

void ArduinoCloudThingBase::begin(const char* name, const char* username, const char* id, const char* password){
    this->name = name;
    this->username = username;
    this->id = id;
    this->password =  password;
}

void ArduinoCloudThingBase::addProperty(const char* name, const char* datatype, const char* permission){
    addExternalProperty(NULL, name, datatype, permission, "", 0);
}

void ArduinoCloudThingBase::addProperty(const char* name, const char* datatype, const char* permission, const char* policy){
    addExternalProperty(NULL, name, datatype, permission, policy, 0);
}

void ArduinoCloudThingBase::addProperty(const char* name, const char* datatype, const char* permission, const char* policy, int lapse){
    addExternalProperty(NULL, name, datatype, permission, policy, lapse);
}

void ArduinoCloudThingBase::addExternalProperty(const char* other_device_name, const char* name, const char* datatype){
    addExternalProperty(other_device_name, name, datatype, RW, "", 0);
}

void ArduinoCloudThingBase::addExternalProperty(const char* other_device_name, const char* name, const char* datatype, const char* permission, const char* policy, int lapse){
    // Create property structure
    property_conf* prop = new property_conf {name, datatype, permission, other_device_name, policy, "", (long)lapse*1000, 0};
    properties[properties_count] = prop; // Save pointer to scructure
    properties_count++; // count the number of properties
}

void ArduinoCloudThingBase::writeProperty(const char* name, String value){
    writeProperty(name, value.c_str());
}

void ArduinoCloudThingBase::writeProperty(const char* name, int value){
    writeProperty(name, String(value).c_str());
}

void ArduinoCloudThingBase::writeProperty(const char* name, float value){
    writeProperty(name, String(value).c_str());
}

void ArduinoCloudThingBase::writeProperty(const char* name, const char* value){
    int i = discoverProperty(NULL, name);

    if (i == -1) {
        // not found, nothing to do
        return;
    }

    if (properties[i]->value.equals(value) && strcmp(properties[i]->policy, ON_CHANGE) == 0) {
        if (cloud_debug) {
            CLOUD_DEBUG_STREAM.print("No Changes for ");
            CLOUD_DEBUG_STREAM.print(name);
            CLOUD_DEBUG_STREAM.print(": ");
            CLOUD_DEBUG_STREAM.println(value);
        }
        return;
    }
    if ((long)(millis() - properties[i]->runtime) >= properties[i]->lapse) {
        properties[i]->value = value;
        String topic = buildTopicProperty(i);

        publish(topic.c_str(), value);

        if (cloud_debug) {
            CLOUD_DEBUG_STREAM.print("OK, Published ");
            CLOUD_DEBUG_STREAM.print(value);
            CLOUD_DEBUG_STREAM.print(" on topic: ");
            CLOUD_DEBUG_STREAM.println(topic);
        }
        properties[i]->runtime = millis();
    }
}

// Get the a property value
String ArduinoCloudThingBase::readProperty(const char* name){
    return readProperty(NULL, name);
}

String ArduinoCloudThingBase::readProperty(const char* _device_name, const char* name){
    int index = discoverProperty(_device_name, name);

    if (index != -1) {
        return String(properties[index]->value);
    }

    return String();
}

void ArduinoCloudThingBase::push(){
    for (int i = 0; i <= properties_count; i++){
        if (properties[i]->device_name == NULL){
            String topic = buildTopicProperty(i);

            publish(topic.c_str(), properties[i]->value.c_str());
        }
    }
}

// Discovers the property position in the array based
// on the name of the property
int ArduinoCloudThingBase::discoverProperty(const char* device_name, const char* name){
    for (int i = 0; i <= properties_count; i++){
        if (properties[i]->name == name && properties[i]->device_name == device_name){
            return i;
        }
    }
    return -1;
}

void ArduinoCloudThingBase::updatePropertyFromTopic(const char* topic, const char* value) {
    for (int i = 0; i <= properties_count; i++){
        String propertyTopic = buildTopicProperty(i);

        if (strcmp(propertyTopic.c_str(), topic) == 0) {
            properties[i]->value = value;
        }
    }
}

// Build the topic for a property
String ArduinoCloudThingBase::buildTopicProperty(int property_index){
    String topic;

    topic += username;
    topic += '/';
    topic += (properties[property_index]->device_name) ? properties[property_index]->device_name : name;
    topic += '/';
    topic += properties[property_index]->name;

    return topic;
}

void ArduinoCloudThingBase::publish(const char * /*topic*/, const char * /*payload*/) {
}


void ArduinoCloudThingBase::enableDebug(){
    cloud_debug = true;
}

void ArduinoCloudThingBase::disableDebug(){
    cloud_debug = false;
}
