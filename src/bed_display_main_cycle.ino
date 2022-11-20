/* Main cycle for the Display System*/

#include "bed_errors.h"
#include <stdio.h>


int32_t b32_error_code = BED_ERR_NONE;


void setup() 
{
  pinMode(BED_SEL_BTN, INPUT);
  pinMode(BED_RESP_BTN, INPUT);
  Serial.begin(57600);

  b32_error_code = bed_init_display();
  Serial.println("Display Status:\t"+ (String)b32_error_code);

  b32_error_code = bed_init_rtc();
  Serial.println("RTC Status:\t"+ (String)b32_error_code);
  
  delay(1000);
  oled.clearDisplay();
}

void loop() 
{
  selState  = digitalRead(BED_SEL_BTN);
  respState = digitalRead(BED_RESP_BTN);            

  //b32_error_code = bed_display_prompt(1);

  if(b32_error_code == BED_ERR_NONE)
  {
    bed_display_info();
    bed_display_date_time();
  }

  else
  {
   Serial.println("Program Failed due to error:\t" + (String)b32_error_code);
  }
}