/* Header file for the RTC System */
#ifndef BED_RTC_H
#define BED_RTC_H
/* Includes */
#include "HardwareSerial.h"
#include "RTClib.h"
#include "Wire.h"
#include "bed_errors.h"

/* Definitions */
#define RTC_ADDRESS          0x68                                                           /* 0x68 for current RTC module */                                                                              

/* Struct Definition*/
typedef struct RTC_Tag
{
  uint16_t    rtc_year;                                                                     /* Represents the year        */  
  uint16_t    rtc_month;                                                                    /* Represents the month       */
  uint16_t    rtc_day;                                                                      /* Represents the day         */
  uint8_t     rtc_hour;                                                                     /* Represents the hour        */  
  uint8_t     rtc_min;                                                                      /* Represents the min         */
  uint8_t     rtc_sec;                                                                      /* Represents the sec         */  
}RTC_DATE_TIME;

/* Global Declaration */
RTC_DS1307 rtc;
DateTime now;
  char daysOfTheWeek[7][12]  ={"Sunday",                                                    /* Represents different days of the week */
                              "Monday", 
                              "Tuesday", 
                              "Wednesday", 
                              "Thursday", 
                              "Friday", 
                              "Saturday"};

char monthsOfTheYear[12][12] = {"January",                                                  /* Represents different months of the year */  
                                "February",
                                "March",
                                "April",
                                "May",
                                "June",
                                "July",
                                "August",
                                "September",
                                "October",
                                "November",
                                "December"};

RTC_DATE_TIME rtc_date_time;                                                                /* Global representation of the rtc object */

/* Function Declarations */
int32_t bed_init_rtc();                                                                     /* Initializes the display system.*/ 
void    bed_set_explicit_date_time(char*, char*);                                           /* Sets date and time to specific values.*/        
void    bed_display_info();                                                                 /* Displays date and time info on the Serial Monitor*/                                                   


#endif