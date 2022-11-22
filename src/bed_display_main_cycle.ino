/* Main cycle for the Display System*/
#include "bed_hardware_pin_map.h"
#include "bed_display.h"
#include "bed_errors.h"
#include "bed_rtc.h"
#include "bed_i2c.h"
#include <stdio.h>


int32_t b32_error_code = BED_ERR_NONE;
bool promptflag = false;

void setup() 
{
  pinMode(BED_SEL_BTN, INPUT);
  pinMode(BED_RESP_BTN, INPUT);
  Serial.begin(BAUD_RATE);

  b32_error_code = bed_init_display();
  Serial.println("Display Status:\t"+ (String)b32_error_code);

  b32_error_code = bed_init_rtc();
  Serial.println("RTC Status:\t"+ (String)b32_error_code);
  
  delay(1000);
  oled.clearDisplay();
}

void loop() 
{
          
  if(b32_error_code == BED_ERR_NONE)
  { 
       promptState = digitalRead(BED_PROMPT_BTN); 
       bed_display_info();
       bed_display_date_time();
       if(promptState == 1)
       {
          bed_display_prompt(1);
          oled.clearDisplay();
       }

  }

  else
  {
   Serial.println("Program Failed due to error:\t" + (String)b32_error_code);
  }
}