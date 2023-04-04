
#ifndef BED_HR_H
#define BED_HR_H

#define USE_ARDUINO_INTERRUPTS false   // Set-up low-level interrupts for most acurate BPM math
#define HEART_EVENT 20 


#include "PulseSensorPlayground.h"     // Includes the PulseSensorPlayground Library
#include <Wire.h>
#include "bed_hardware_pin_map.h"

unsigned long HRtime  = 0;

const uint16_t Threshold = 550;           // Determine which Signal to "count as a beat" and which to ignore
uint16_t BPM = 0;

#endif 