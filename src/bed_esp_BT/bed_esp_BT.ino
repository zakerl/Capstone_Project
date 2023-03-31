#include "bed_sd.h"
#include <string.h>
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Bluetooth not available or not enabled. It is only available for the ESP32 chip.
#endif

unsigned long start_millis;  
unsigned long current_millis;
const unsigned long period = 5000;  //the value is a number of milliseconds 
bool data_sent = false;
char data[200];
// String data;

void setup() {
  Serial.begin(115200);
  start_millis = millis();
  SerialBT.begin("ESP32-WROOM"); //Bluetooth device name
  if(!SD.begin(5)){
    Serial.println("Card Mount Failed");
    return;
  }

  uint8_t cardType = SD.cardType();

  if(cardType == CARD_NONE){
    Serial.println("No SD card attached");
    return;
  }
}

void recieve_BT_data(){
  if (SerialBT.available()) {
    char incoming_data = SerialBT.read();
    Serial.println(incoming_data);
    // Serial.write(SerialBT.read());
    data[-1] = incoming_data;
    appendFile(SD,"/config.txt",data);
  }
}

void loop() {
  current_millis = millis();
  recieve_BT_data();
  if (current_millis - start_millis >=period){ 
      if (SerialBT.available()) {
        readFile(SD, "/dataview.txt");
        start_millis = current_millis;
      }
  }
}

