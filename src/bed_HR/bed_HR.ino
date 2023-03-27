#define USE_ARDUINO_INTERRUPTS true    // Set-up low-level interrupts for most acurate BPM math
#define HEART_EVENT 20 

#include <PulseSensorPlayground.h>     // Includes the PulseSensorPlayground Library
#include <Wire.h>
#include "bed_HR.h"

PulseSensorPlayground pulseSensor;  // Creates an object

void setup(void){

}
void loop(void){
  
}

void bed_HR_setup() {
  Serial.begin(19200);
  
  // Configure the PulseSensor object, by assigning our variables to it
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);       // Blink on-board LED with heartbeat
  pulseSensor.setThreshold(Threshold);   

  // Double-check the "pulseSensor" object was created and began seeing a signal
  if (pulseSensor.begin()) {
    Serial.println("PulseSensor object created");
  }

  BPM_Struct.BPM = pulseSensor.getBeatsPerMinute();

}

// This should be triggered whenever you want to measure heartrate. Make sure that the setup is done first.
void bed_HR_detect() {
  // put your main code here, to run repeatedly:
  unsigned long currentMillis = millis(); // Gets the current time
  if(currentMillis - HRtime >= HEART_EVENT){
    BPM_Struct.BPM = pulseSensor.getBeatsPerMinute();      // Calculates BPM
    
    if (pulseSensor.sawStartOfBeat()) {               // Constantly test to see if a beat happened
      Serial.println("HeartBeat Detected "); // If true, pruint8_t a message
      Serial.print("BPM: ");
      Serial.println(BPM_Struct.BPM);                        // Pruint8_t the BPM value
      }
    HRtime = currentMillis;
  }

}
