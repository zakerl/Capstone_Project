/* Implementation file for RTC driver*/

#include "bed_rtc.h"

/*
    Author    : Anish Rangarajan
    Date      : 11/16/2022
    Defintion : Initializes the rtc system.
*/
int32_t bed_init_rtc()
{
  int32_t b32_error_code = BED_ERR_NONE;
  b32_error_code = bed_get_i2c_status(RTC_ADDRESS);
    
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

  return b32_error_code;
}

/*
    Author    : Anish Rangarajan
    Date      : 11/16/2022
    Defintion : Displays date and time info on the Serial Monitor
*/

void bed_display_info()
{
    DateTime now = rtc.now();
    rtc_date_time.rtc_year   = now.year();
    rtc_date_time.rtc_month  = now.month();
    rtc_date_time.rtc_day    = now.day();
    rtc_date_time.rtc_hour   = now.hour();
    rtc_date_time.rtc_min    = now.minute();
    rtc_date_time.rtc_sec    = now.second();
    Serial.print(now.year(), DEC);
    Serial.print('/');
    Serial.print(now.month(), DEC);
    Serial.print('/');
    Serial.print(now.day(), DEC);
    Serial.print("(");
    Serial.print(daysOfTheWeek[now.dayOfTheWeek()]);
    Serial.print(") ");
    Serial.print(now.hour(), DEC);
    Serial.print(':');
    Serial.print(now.minute(), DEC);
    Serial.print(':');
    Serial.print(now.second(), DEC);
    Serial.println();
    delay(1000);
}
/*
    Author    : Anish Rangarajan
    Date      : 11/16/2022
    Defintion : Sets date and time to specific values.
                Date string, e.g. "Apr 16 2020".
                Time string, e.g. "18:34:56".
*/
void bed_set_explicit_date_time(char* date, char* time) 
{
  rtc.adjust(DateTime(date,time));
}







































//