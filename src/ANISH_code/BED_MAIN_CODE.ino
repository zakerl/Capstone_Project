/* Main cycle for the Display System*/
#include "bed_hardware_pin_map.h"
#include "bed_touch.h"
#include "bed_display.h"
#include "bed_errors.h"
#include "bed_i2c.h"
#include <stdio.h>
#include <string.h>
int8_t input = 0;
int8_t state = -1;
uint8_t clear = 0;

/* Inputs Macros*/
#define CLOCKWISE_INPUT            1
#define COUNTER_CLOCKWISE_INPUT   -1
#define KEY_0_INPUT                2
#define KEY_1_INPUT                5
#define KEY_2_INPUT                3
#define KEY_4_INPUT                4

/* State Macros*/
#define START_STATE               -1 
#define IDLE_STATE                 0
#define DATE_TIME_STATE            1
#define PROMPT_STATE               2
#define HOME_STATE                 3

int8_t changeState(int8_t input)
{
  switch(input)
    {

      case  COUNTER_CLOCKWISE_INPUT:
      case  CLOCKWISE_INPUT:
              if(clear)
                tft.fillScreen(GC9A01A_BLACK);
              state = 0;
              clear = 0;
              break;

      case  KEY_0_INPUT:
             Serial.println(input);
             tft.fillScreen(GC9A01A_BLACK);
             state = 1;
             clear = 1;
             break;
      
      case  KEY_2_INPUT:
             Serial.println(input);
             tft.fillScreen(GC9A01A_BLACK);
             state = 2;
             clear = 1;
             break;

      case  KEY_4_INPUT:
             Serial.println(input);
             tft.fillScreen(GC9A01A_BLACK);
             state = 3;
             clear = 1;
             break;         

    } 
    return state;
}

void setState(int8_t state)
{
    switch (state)
    {
      case START_STATE:
              bed_splash_screen();
              clear = 1;
              break;

      case IDLE_STATE:
              bed_scroll_test(input,6,0);
              break;
      case DATE_TIME_STATE:
              bed_display_info();
              bed_display_date_time();
              break;

      case PROMPT_STATE:
              bed_display_prompt(input,1);
              break;
      case HOME_STATE:
              bed_splash_screen();
              clear = 1;
              break;
    }


}


void setup() 
{
  int32_t b32_error_code = BED_ERR_NONE;
  Serial.begin(BAUD_RATE);
  pinMode(BED_TOUCH_PAD_0, INPUT);
  pinMode(BED_TOUCH_PAD_1, INPUT);
  pinMode(BED_TOUCH_PAD_2, INPUT);
  pinMode(BED_TOUCH_PAD_3, INPUT);
  pinMode(BED_TOUCH_PAD_4, INPUT);

  b32_error_code = bed_init_display();
  Serial.println("Display Status:\t" + (String)b32_error_code);

  if(b32_error_code == BED_ERR_NONE)
  {
    b32_error_code = bed_init_rtc();    
    Serial.println("RTC Status:\t" + (String)b32_error_code);
  }
  if(b32_error_code == BED_ERR_NONE)
  {
    b32_error_code = bed_init_MPU();    
    Serial.println("MPU Status:\t" + (String)b32_error_code);
  }
  // if(b32_error_code == BED_ERR_NONE)
  // {
  //   b32_error_code = bed_init_HR();    
  //   Serial.println("HR Status:\t" + (String)b32_error_code);
  // }
}


void loop() 
{
  int8_t limp_flag = 0;
  unsigned long currentTime = millis();

  if (currentTime - prev_touch_time >= TOUCH_SAMPLE_TIME) 
  {
    touchval[0] = digitalRead(BED_TOUCH_PAD_4);
    touchval[1] = digitalRead(BED_TOUCH_PAD_3);
    touchval[2] = digitalRead(BED_TOUCH_PAD_2);
    touchval[3] = digitalRead(BED_TOUCH_PAD_1);
    touchval[4] = digitalRead(BED_TOUCH_PAD_0);

    input = bed_touch_detect(currentTime);
    Serial.println(input);
    prev_touch_time = currentTime;

    state = changeState(input);
    
  }
  // I DON'T KNOW IF I'M DOING THIS RIGHT

  if(currentTime - MPULooptime >= MPU_EVENT)
  {
      limp_flag = bed_MPU_detect();
      MPULooptime = currentTime;

  } 
  if(limp_flag == 1){
    input = KEY_2_INPUT;
  }
  if(limp_flag == -1 && real_heart_rate >= 100){
    input = KEY_2_INPUT;
  }

  // if(currentMillis - HRtime >= HEART_EVENT){
  //   bed_HR_detect();
  //   HRtime = currentMillis;
  // }
  setState(state);
}
















///