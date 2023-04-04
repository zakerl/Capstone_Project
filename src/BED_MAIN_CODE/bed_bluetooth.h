/*==========================================
 Title:  BED Bluetooth Header for ESP32 
 Author: Nish Shah
 Date:   4 April 2023
==========================================*/
#ifndef BED_BTH_H
#define BED_BTH_H
#include "bed_sd.h"

#include <string.h>
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)


#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Bluetooth not available or not enabled. It is only available for the ESP32 chip.
#endif

unsigned long prev_bth_time = 0;
const uint16_t BTH_SAMPLE_TIME = 5000;  //the value is a number of milliseconds 
bool data_sent = false;
char data[200];


void recieve_BT_data(){
  if (SerialBT.available()) {
    char incoming_data = SerialBT.read();
    Serial.println(incoming_data);
    // Serial.write(SerialBT.read());
    data[-1] = incoming_data;
    appendFile(SD,"/config.txt",data);
  }
}

#endif
