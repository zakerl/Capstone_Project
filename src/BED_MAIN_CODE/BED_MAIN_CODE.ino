
/* Main cycle for the Display System*/
#include "bed_hardware_pin_map.h"
#include "bed_touch.h"
#include "bed_prompt.h"
#include "bed_display.h"
#include "bed_errors.h"
#include "bed_rtc.h"
#include "bed_HR.h"
#include "bed_i2c.h"
#include <stdio.h>
#include <string.h>
#include "bed_bluetooth.h"
#include "bed_mpu.h"

int8_t input = 0;
int8_t currstate;
uint8_t clear = 0;
uint8_t prompt_index_walk = 0;
uint8_t prompt_index_alarm = 0;

/* Inputs Macros*/
#define COUNTER_CLOCKWISE_INPUT   -1
#define NO_UPDATE                  0
#define CLOCKWISE_INPUT            1

#define KEY_4_INPUT                2
#define KEY_3_INPUT                3
#define KEY_2_INPUT                4
#define KEY_1_INPUT                5
#define KEY_0_INPUT                6
#define ALARM_INPUT                7 

/* State Macros*/
#define START_STATE                40  
#define DATE_TIME_STATE            41
#define PROMPT_STATE               42
#define HOME_STATE                 43
#define ALARM_PROMPT_STATE         44 

/* Takes inputs and changes state*/
int8_t changeState(int8_t input)
{
  switch(input)
    {

      case  COUNTER_CLOCKWISE_INPUT:
      case  CLOCKWISE_INPUT:
              break;

      case 0:
              break;

      case  KEY_0_INPUT:
             currstate  = HOME_STATE;
             clear      = 0;
             draw_flag  = 0;
             break;
      
      case  KEY_2_INPUT:
             currstate = DATE_TIME_STATE;
             clear      = 0;;
             draw_flag  = 0;
             break;

      case  KEY_4_INPUT:
             currstate = PROMPT_STATE;
             clear      = 0;
             draw_flag  = 0;
             break;    

      case ALARM_INPUT:
             currstate = ALARM_PROMPT_STATE;
             clear      = 0;
             draw_flag  = 0;
             break;                     

    } 
    return currstate;
}


/* Used to set the state of the system */
void setState(int8_t state)
{
    switch (state)
    {
      case START_STATE:
              bed_splash_screen();
              currstate = NO_UPDATE;
              break;

      case NO_UPDATE:
              break;
              
      case DATE_TIME_STATE:
              alarm_flag = 0;      
              if(!clear)
              {
                tft.fillScreen(GC9A01A_BLACK);
                clear = 1;
              }
              bed_display_date_time();
              break;

      case PROMPT_STATE:
              if(!clear)
              {
                tft.fillScreen(GC9A01A_BLACK);
                clear = 1;
              }

              bed_display_prompt(input,prompt_index_walk,prompt_walking[prompt_index_walk].no_of_options,1);
              break;

      case HOME_STATE:
              draw_flag = 0;
              clear = 0;
              tft.fillScreen(GC9A01A_BLACK);
              bed_splash_screen();
              currstate = NO_UPDATE;
              break;

      case ALARM_PROMPT_STATE:
              if(!clear)
              {
                tft.fillScreen(GC9A01A_BLACK);
                clear = 1;
                draw_flag = 0;
              }

              bed_display_prompt(input,prompt_index_alarm,prompt_alarm[prompt_index_alarm].no_of_options,2);
              break;
    }

}


void setup() 
{
  int32_t b32_error_code = BED_ERR_NONE;
  Serial.begin(BAUD_RATE);
 //bed_HR_setup();
  pinMode(BED_SD_CS,OUTPUT);
  pinMode(BED_TFT_CS, OUTPUT);
  pinMode(BED_TOUCH_PAD_0, INPUT);
  pinMode(BED_TOUCH_PAD_1, INPUT);
  pinMode(BED_TOUCH_PAD_2, INPUT);
  pinMode(BED_TOUCH_PAD_3, INPUT);
  pinMode(BED_TOUCH_PAD_4, INPUT);

  currstate = DATE_TIME_STATE;

  // if(!SD.begin(14)){
  //   Serial.println("Card Mount Failed");
  //   return;
  // }

  // else {
  // Serial.println("Works");
  
  // }
  // uint8_t cardType = SD.cardType();
  // if(cardType == CARD_NONE)
  // {
  //   Serial.println("No SD card attached");
  // }
  // char message3[50] = "Nish very gay";
  // writeFile("/dataview.txt", message3);
  // readFile(SD, "/dataview.txt");

  b32_error_code = bed_init_display();
  Serial.println("Display Status:\t" + (String)b32_error_code);
  if(b32_error_code == BED_ERR_NONE)
  {
    b32_error_code = bed_init_rtc();    
    Serial.println("RTC Status:\t" + (String)b32_error_code);


  }

  if(b32_error_code == BED_ERR_NONE)
    {
      b32_error_code = bed_MPU_setup();    
      Serial.println("MPU Status:\t" + (String)b32_error_code);
    }

  //SerialBT.begin("ESP32-WROOM-ANISH"); //Bluetooth device name
}

void loop() 
{

  unsigned long currentTime = millis();
  //recieve_BT_data();
  
  /* Grabs touch sensor data and changes state based on touch input*/
  if (currentTime - prev_touch_time >= TOUCH_SAMPLE_TIME) 
  {
    touchval[0] = digitalRead(BED_TOUCH_PAD_4);
    touchval[1] = digitalRead(BED_TOUCH_PAD_3);
    touchval[2] = digitalRead(BED_TOUCH_PAD_2);
    touchval[3] = digitalRead(BED_TOUCH_PAD_1);
    touchval[4] = digitalRead(BED_TOUCH_PAD_0);
  
    input = bed_touch_detect(currentTime);
    
    input = bed_alarm_prompt(input);

    prev_touch_time = currentTime;    
    currstate = changeState(input);
    setState(currstate);
  }

  /* Grabs MPU data and updates footsteps*/
  if(currentTime - MPULooptime >= MPU_EVENT)
  {
    bed_MPU_detect(currentTime);
    MPULooptime = currentTime;
  }

  // if (currentTime- prev_bth_time >= BTH_SAMPLE_TIME){ 
  //     if (SerialBT.available()) {
  //       readFile(SD, "/dataview.txt");
  //       prev_bth_time = currentTime;
  //     }
  // }

/*
  if(currentTime - HRtime >= HEART_EVENT)
  {
    bed_HR_detect(); 
    HRtime = currentTime;
  }
*/ 
}














///