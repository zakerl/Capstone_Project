/* Implementation file for RTC driver*/

#include "bed_rtc.h"

/* 
  Initializes the RTC
  Params : N/A
  Outputs: Error Code.
*/
int32_t bed_init_rtc()
{
  int32_t b32_error_code = BED_ERR_NONE;
  //b32_error_code = bed_get_i2c_status(RTC_ADDRESS);
    
  if (! rtc.begin())
  { 
    Serial.println("Couldn't find RTC");
    b32_error_code = BED_ERR_RTC_SYSTEM;
    Serial.flush();
    while (1) delay(10);
  }

  else if (! rtc.isrunning()) 
  {
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }

  else 
    b32_error_code = BED_ERR_NONE;
  

  return b32_error_code;
}

/* 
  Stores all RTC info into the struct
  Params : N/A
  Outputs: N/A
*/

void bed_display_info()
{
    now = rtc.now();
    rtc_date_time.rtc_year   = now.year();
    rtc_date_time.rtc_month  = now.month();
    rtc_date_time.rtc_day    = now.day();
    rtc_date_time.rtc_hour   = now.hour();
    rtc_date_time.rtc_min    = now.minute();
    rtc_date_time.rtc_sec    = now.second();
}

int8_t curr_alarm = -1;

/* 
  Generates prompt when alarm is reached.
  Params : prev_input : Previous state of the system.
  Outputs: new_input  : New state of the system.
*/
int8_t bed_alarm_prompt(int8_t prev_input)
{
  int8_t new_input;

  for(int i =0; i < 3;i++)
  {
        if(rtc_date_time.rtc_hour == alarms[i][0] && rtc_date_time.rtc_min == alarms[i][1] && alarm_flag == 0 ) 
          {
            if(i != curr_alarm)
            {
              curr_alarm = i;
              new_input = ALARM_INPUT;
              alarm_flag = 1;
              return new_input;              
            }
          } 
  }

  return prev_input;
}

/* 
  Sets date and time to a specific value.
  Params : date: Date string.
           time: time string.
  Outputs: Error Code.
*/
void bed_set_explicit_date_time(char* date, char* time) 
{
  rtc.adjust(DateTime(date,time));
}







































//