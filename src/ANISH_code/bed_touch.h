/* Header file for the touch sensors used in the system */
#ifndef BED_TOUCH_H
#define BED_TOUCH_H

#define NO_OF_KEYS 5              /* Represents number of touch keys used*/
#define TOUCH_SAMPLE_TIME 5    /* Sample time for touch sensor values*/
#define TOUCH_WAIT_TIME 150    /* Sample time for touch sensor values*/
#define TOUCH_MIN_WAIT_TIME 20

/* Struct Declaration*/

typedef struct Touch_Tag
{
  int8_t  flag = -1;                  /* Flag to represent state machine of the touch sensor*/
  int8_t  pad_is_touched_first = -1;  /* Represents first key pressed*/
  int8_t  pad_is_touched_second = -1; /* Represents second key pressed*/
  int8_t  direction = 0;              /* Represents orientation 1(CW) -1(CCW)*/
  uint8_t releaseFlag = 1;
}Touch;

/* Global Declaration*/

uint16_t touchval[NO_OF_KEYS];
uint16_t firsttouch[NO_OF_KEYS];
unsigned long prev_touch_time = 0;
unsigned long prev_wait_time = 0;


Touch touch;


/* Function Prototypes*/
int8_t bed_touch_detect(unsigned long);
#endif