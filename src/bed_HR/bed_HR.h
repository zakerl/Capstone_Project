#ifndef BED_HR_H
#define BED_HR_H
unsigned long HRtime = 0;
const uint8_t PulseWire = 0;       // 'S' Signal pin connected to A0
const uint8_t LED13 = 13;          // The on-board Arduino LED
const uint16_t Threshold = 550;           // Determine which Signal to "count as a beat" and which to ignore

struct {
  uint16_t BPM = 0;
  uint16_t BPM_Avg = 0;
} BPM_Struct;


#endif 