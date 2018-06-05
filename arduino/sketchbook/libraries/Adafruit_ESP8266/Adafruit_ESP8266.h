/*------------------------------------------------------------------------
  An Arduino library for the ESP8266 WiFi-serial bridge

  https://www.adafruit.com/product/2282

  The ESP8266 is a 3.3V device.  Safe operation with 5V devices (most
  Arduino boards) requires a logic-level shifter for TX and RX signals.

  Adafruit invests time and resources providing this open source code,
  please support Adafruit and open-source hardware by purchasing
  products from Adafruit!

  Written by Limor Fried and Phil Burgess for Adafruit Industries.
  MIT license, all text above must be included in any redistribution.
  ------------------------------------------------------------------------*/

#ifndef _ADAFRUIT_ESP8266_H_
#define _ADAFRUIT_ESP8266_H_

#include <Arduino.h>

#define ESP_RECEIVE_TIMEOUT   1000L
#define ESP_RESET_TIMEOUT     5000L
#define ESP_CONNECT_TIMEOUT  15000L
#define ESP_IPD_TIMEOUT     120000L

typedef const __FlashStringHelper Fstr; // PROGMEM/flash-resident string
typedef const PROGMEM char        Pchr; // Ditto, kindasorta

#define defaultBootMarker F("ready\r\n")

// Subclassing Print makes debugging easier -- output en route to
// WiFi module can be duplicated on a second stream (e.g. Serial).
class Adafruit_ESP8266 : public Print {
 public:
  Adafruit_ESP8266(Stream *s = &Serial, Stream *d = NULL, int8_t r = -1);
  boolean   hardReset(void),
            softReset(void),
            find(Fstr *str = NULL, boolean ipd = false),
            connectToAP(Fstr *ssid, Fstr *pass),
            connectTCP(Fstr *host, int port),
            requestURL(Fstr *url),
            requestURL(char* url);
  int       readLine(char *buf, int bufSiz);
  void      closeAP(void),
            closeTCP(void),
            debugLoop(void),
            setDebug(Stream *d = NULL),
            setTimeouts(uint32_t rcv = ESP_RECEIVE_TIMEOUT,
                        uint32_t rst = ESP_RESET_TIMEOUT,
                        uint32_t con = ESP_CONNECT_TIMEOUT,
                        uint32_t ipd = ESP_IPD_TIMEOUT),
            setBootMarker(Fstr *s = NULL);
 private:
  Stream   *stream,     // -> ESP8266, e.g. SoftwareSerial or Serial1
           *debug;      // -> host, e.g. Serial
  uint32_t  receiveTimeout, resetTimeout, connectTimeout, ipdTimeout;
  int8_t    reset_pin;  // -1 if RST not connected
  Fstr     *host,       // Non-NULL when TCP connection open
           *bootMarker; // String indicating successful boot
  boolean   writing;
  virtual size_t write(uint8_t); // Because Print subclass
};

#endif // _ADAFRUIT_ESP8266_H_
