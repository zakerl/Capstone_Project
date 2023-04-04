/*==========================================
 Title:  BED Bluetooth Test for ESP32 
 Author: Nish Shah
 Date:   4 April 2023
==========================================*/
#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Bluetooth not available or not enabled. It is only available for the ESP32 chip.
#endif

BluetoothSerial SerialBT;
unsigned long start_millis;  
unsigned long current_millis;
const unsigned long period = 5000;  //the value is a number of milliseconds 
bool data_sent = false;

void readFile(fs::FS &fs, const char * path){
  Serial.println("ReadFile called");
  File file = fs.open(path);
  if(!file){
    SerialBT.println("File not available");
    return;
  }
  while(file.available()){
      if (SerialBT.available()) {
        SerialBT.write(file.read());
      }
  }
  file.close();
}


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

void loop() {
  current_millis = millis();
  if (current_millis - start_millis >=period){ 
        readFile(SD, "/dataview.txt");
        start_millis = current_millis;
  }
}


