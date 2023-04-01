#ifndef BED_HR_H
#define BED_HR_H
#define USE_ARDUINO_INTERRUPTS false    // Set-up low-level interrupts for most acurate BPM math
#define HEART_EVENT 20 

const int OUTPUT_TYPE = SERIAL_PLOTTER;

const int PULSE_INPUT = 27;
const int PULSE_BLINK = 2;
const int PULSE_FADE = 5;
const int THRESHOLD = 2000;   // Adjust this number to avoid noise when idle

byte samplesUntilReport;
const byte SAMPLES_PER_SERIAL_SAMPLE = 10;

struct {
  uint16_t BPM = 0;
  uint16_t BPM_Storage[10];
  uint16_t BPM_Avg = 0;
  uint16_t BPM_Sum = 0;
} BPM_Struct;


#endif 