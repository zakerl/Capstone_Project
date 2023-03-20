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

void readFile(fs::FS &fs, const char * path){
  File file = fs.open(path);
  if(!file){
    SerialBT.println("Failed to open file for reading");
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
  readFile(SD, "/dataview.txt");
}

void loop() {
  // if (Serial.available()) {
  //   SerialBT.write(Serial.read());
  // }
  // if (SerialBT.available()) {
  //   Serial.write(SerialBT.read());
  // }

  delay(1000*10);
}
