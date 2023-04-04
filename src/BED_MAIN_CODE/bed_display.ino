#include "SPI.h"
#include "Adafruit_GFX.h"
#include "Adafruit_GC9A01A.h"
#include "bed_display.h"
#include "bed_prompt.h"
#include "bed_rtc.h"
#include "bed_sd.h"
int8_t curr_hr = -1, curr_min = -1, curr_sec = -1;
uint8_t wait_flag = 0;
char prompt_buff[20] = ""; 
char inPain[10] = "";

/* 
  Initializes display 
  Params : N/A 
  Outputs: Error code 
*/

int32_t bed_init_display()
{
  int32_t b32_error_code = BED_ERR_NONE;
  tft.begin();
  tft.setRotation(2);
  bed_splash_screen(); 
  tft.fillScreen(GC9A01A_BLACK);
  return b32_error_code;
}


/* 
  Displays prompt based on type
  Params : direction      : Input coming from the touch sensor.
           prompt_index   : Text that the prompt will display.
           no_of_options  : No of options for specific prompt.
           flag           : Type of prompt (Alarm or Walk).   

  Outputs: N/A
*/

void bed_display_prompt(int8_t direction, uint8_t prompt_index,  uint8_t no_of_options, uint8_t flag)
{
  tft.setTextSize(1);
  uint8_t cursorPosX[2] = {110, 90};
  uint8_t cursorPosY[no_of_options];
  char options[50];
  uint16_t offset = tft.height()/no_of_options;

  if(draw_flag == 0)
  {
    tft.setTextColor(GC9A01A_CYAN);
    tft.setTextSize(1);
    tft.setCursor(20, tft.height()/2);
    switch(flag)
    {
      case 1:
            tft.print(prompt_walking[prompt_index].prompt_question); 
            break;
      case 2:
            tft.print(prompt_alarm[prompt_index].prompt_question); 
            break;
    }
    
    draw_flag = 1;
    wait_flag = 0;
  }

  if(draw_flag == 1 && wait_flag == 0)
  {
    if(direction == 1 || direction == -1)
    {
      wait_flag = 1;
      draw_flag = 0;
      tft.fillScreen(GC9A01A_BLACK);
    }
  }

  if(wait_flag == 1)
  {
    for( uint8_t i=0,j=1; i < no_of_options && j<= no_of_options; i++,j++)
      {
        cursorPosY[i] = j*offset  - 20 ;

          if(draw_flag == 0)
          {   
            if(flag == 0)
            {
              sprintf(options,"%d",j);
              bed_display_one_line(options, cursorPosX[0]  , cursorPosY[i], false);
            }
              

            else if(flag == 1)
            {
              bed_display_one_line(prompt_walking[prompt_index].prompt_possible_answers[i], cursorPosX[0]  , cursorPosY[i], false);  
            }

            else if(flag == 2)
            {
              bed_display_one_line(prompt_alarm[prompt_index].prompt_possible_answers[i], cursorPosX[0]  , cursorPosY[i], false);  
            }
          }  
      }
    draw_flag = 1;

    if(direction == 5)
    {
      /* Store answer into SD*/
    
      switch(flag) 
      {
        case 1:
              //Serial.println(prompt_walking[prompt_index].prompt_possible_answers[scroll_index]);
              if(!strcmp(prompt_walking[prompt_index].prompt_possible_answers[scroll_index],"Pain") || prompt_index_walk == 1)
              {
                char temp_buff[50];
                prompt_index_walk += 1;
                currstate = changeState(KEY_4_INPUT); 
                strcpy(temp_buff,prompt_walking[prompt_index].prompt_possible_answers[scroll_index]);
                strcpy(inPain,"Yes");
                strcat(prompt_buff,",");
                strcat(prompt_buff, temp_buff);
              }

              else
              {
                
                if(strlen(prompt_buff) == 0) 
                {
                  sprintf(prompt_buff,",%s,NULL,NULL",prompt_walking[prompt_index].prompt_possible_answers[scroll_index]);
                  strcpy(inPain,"No");
                } 

                else 
                {
                  char temp_buff[50];
                  prompt_index_walk += 1;
                  currstate = changeState(KEY_4_INPUT); 
                  strcpy(temp_buff,prompt_walking[prompt_index].prompt_possible_answers[scroll_index]);
                  strcat(prompt_buff,",");
                  strcat(prompt_buff, temp_buff);
                }

                currstate = changeState(KEY_2_INPUT);
                prompt_index_walk = 0;
                char buff[100];
                sprintf(buff,"%d-%d-%d,%d:%d,%d,%d,%d,%s,%s%s",rtc_date_time.rtc_day,rtc_date_time.rtc_month,rtc_date_time.rtc_year,rtc_date_time.rtc_hour,rtc_date_time.rtc_min,100,30,12,"Walk",inPain,prompt_buff);
                Serial.println(buff);
                //writeFile(SD, "/dataview.txt", buff);
                //readFile(SD, "/dataview.txt");
                strcpy(prompt_buff,"");
              }
              break;

        case 2:
              if(!strcmp(prompt_alarm[prompt_index].prompt_possible_answers[scroll_index],"Yes") || prompt_index_alarm == 1)
              {

                char temp_buff[50];
                prompt_index_walk += 1;
                currstate = changeState(KEY_4_INPUT); 

                strcpy(temp_buff,prompt_alarm[prompt_index].prompt_possible_answers[scroll_index]);
                strcat(prompt_buff,",");
                strcat(prompt_buff, temp_buff);    
                if(prompt_index_alarm == 0)
                {
                  strcat(prompt_buff, ",NULL");
                }
                prompt_index_alarm += 1;
                currstate = changeState(ALARM_INPUT);
              }

              else
              {
                if(strlen(prompt_buff) == 0) 
                {
                  sprintf(prompt_buff,",%s,NULL,NULL,NULL",prompt_alarm[prompt_index].prompt_possible_answers[scroll_index]);
                }
                else
                {
                  char temp_buff[50];
                  prompt_index_walk += 1;
                  currstate = changeState(ALARM_INPUT); //VERIFY IF CHANGE IS CORRECT
                  strcpy(temp_buff,prompt_alarm[prompt_index].prompt_possible_answers[scroll_index]);
                  strcat(prompt_buff,",");
                  strcat(prompt_buff, temp_buff);
                }
                currstate = changeState(KEY_2_INPUT);
                prompt_index_alarm = 0;
                char buff[100];
                sprintf(buff,"%d-%d-%d,%d:%d,%d,%d,%d,%s%s",rtc_date_time.rtc_day,rtc_date_time.rtc_month,rtc_date_time.rtc_year,rtc_date_time.rtc_hour,rtc_date_time.rtc_min,100,30,12,"Alarm",prompt_buff);
                Serial.println(buff);
                strcpy(prompt_buff,"");
              }
              break;

      }

    

    }


  if(direction == -1 || direction == 1)
  {
    if(scroll_index + direction > no_of_options-1 )
    {
      tft.fillRect(cursorPosX[1], cursorPosY[scroll_index]-15, CURSOR_WIDTH, CURSOR_HEIGHT,GC9A01A_BLACK);
      yield();
      scroll_index = 0;
      tft.fillRect(cursorPosX[1], cursorPosY[scroll_index]-15, CURSOR_WIDTH, CURSOR_HEIGHT,GC9A01A_ORANGE);
      yield();    
    }

    else if(scroll_index + direction < 0 )
    {
      tft.fillRect(cursorPosX[1], cursorPosY[scroll_index]-15, CURSOR_WIDTH, CURSOR_HEIGHT,GC9A01A_BLACK);
      yield();
      scroll_index = no_of_options-1;
      tft.fillRect(cursorPosX[1], cursorPosY[scroll_index]-15, CURSOR_WIDTH, CURSOR_HEIGHT,GC9A01A_ORANGE);
      yield();    
    }

    else
    {
      tft.fillRect(cursorPosX[1], cursorPosY[scroll_index + direction]-15, CURSOR_WIDTH, CURSOR_HEIGHT,GC9A01A_ORANGE);
      yield();
      tft.fillRect(cursorPosX[1], cursorPosY[scroll_index]-15, CURSOR_WIDTH, CURSOR_HEIGHT,GC9A01A_BLACK);
      yield();
      scroll_index = scroll_index + direction;
    }
  }  
}
  

}


/* 
  Displays startup screen
  Params : N/A                     
  Outputs: N/A
*/
void bed_splash_screen()
{
  tft.setFont(&FreeSans9pt7b);
  tft.setTextSize(2);

  if(draw_flag == 0)
  {
      bed_display_one_line("Back"       , tft.width()/7.5, tft.height()/3 + 10, false);
      bed_display_one_line("End"        , tft.width()/7.5, tft.height()/2 + 10, false);
      bed_display_one_line("Developers" , tft.width()/7.5, tft.height()/1.5 + 10, false);
  }

  yield();
}

/* 
  Displays text on specific line of the display
  Params : displayText      : Text to be displayed.
           coordX           : X coordinate on the screen.
           coordY           : Y coordinate on the screen.
           clearFlag        : Flag which controls screen clear. 

  Outputs: N/A
*/

void bed_display_one_line(char* displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag)
{
  if(clearFlag)
    tft.fillScreen(GC9A01A_BLACK);
    
  tft.setTextColor(GC9A01A_WHITE);
  tft.setCursor(coordX, coordY);
  tft.print(displayText);

}

/* 
  Displays text on specific line of the display with specific color
  Params : displayText      : Text to be displayed.
           coordX           : X coordinate on the screen.
           coordY           : Y coordinate on the screen.
           clearFlag        : Flag which controls screen clear.
           textColor        : Color of text to be displayed.

  Outputs: N/A
*/
void bed_display_one_line(char* displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag, uint8_t textColor){
  if(clearFlag)
    tft.fillScreen(GC9A01A_BLACK);
    
  tft.setTextColor(GC9A01A_WHITE);
  tft.setCursor(coordX, coordY);
  tft.setTextSize(2);
  tft.setFont(&FreeSans9pt7b);
  tft.println(displayText);
}

/* 
 Draws the hour for the RTC on startup
  Params : N/A
  Outputs: N/A
*/
void drawHour()
{
   tft.setTextSize(4);
    tft.setFont(&FreeSans9pt7b);
    tft.setTextColor(GC9A01A_ORANGE);
    tft.setCursor(20,tft.height()/2 + 20);

    if(rtc_date_time.rtc_hour < 10)
    {
      tft.print(0);
      tft.print(rtc_date_time.rtc_hour);
    }
    else
    {
      tft.print(rtc_date_time.rtc_hour); 
    }  
}

/* 
 Draws the minute for the RTC on startup
  Params : N/A
  Outputs: N/A
*/
void drawMinute()
{
  if(rtc_date_time.rtc_min < 10)
    {
      tft.print(0);
      tft.print(rtc_date_time.rtc_min);
    }
    else
    {
      tft.print(rtc_date_time.rtc_min); 
    }  
}

/* 
 Draws the second for the RTC on startup
  Params : N/A
  Outputs: N/A
*/
void drawSecond()
{
    tft.setCursor(205,tft.height()/2 -20);
    tft.setTextSize(1);
    tft.setTextColor(GC9A01A_WHITE);

    if(rtc_date_time.rtc_sec < 10)
    {
      tft.print(0);
      tft.print(rtc_date_time.rtc_sec);
    }
    else
    {
      tft.print(rtc_date_time.rtc_sec); 
    }  
}

/* 
  Displays the current date and time.
  Params : N/A
  Outputs: N/A
*/
void bed_display_date_time()
{
  bed_display_info();
  /* Updates the date on startup*/
  if(draw_flag == 0)
  { 
    tft.drawCircle(tft.width()/2, tft.height()/2, tft.width()/2 - 15, GC9A01A_CYAN);

    drawHour();
    tft.setCursor(105,tft.height()/2 + 20);
    tft.print(":"); 
    drawMinute();
    drawSecond();
    draw_flag = 1;
  }

  /* Hour */
  tft.setTextSize(4);
  tft.setFont(&FreeSans9pt7b);
  tft.setTextColor(GC9A01A_ORANGE);
  tft.setCursor(20,tft.height()/2 + 20);

  /* Hour */ 
  if(rtc_date_time.rtc_hour != curr_hr)
  {

    tft.fillRect(28, tft.height()/2- 40,75,70,GC9A01A_BLACK);
    if(rtc_date_time.rtc_hour < 10)
    {
      tft.print(0);
      tft.print(rtc_date_time.rtc_hour);
    }
    else
    {
      tft.print(rtc_date_time.rtc_hour); 
    }  
    curr_hr = rtc_date_time.rtc_hour;

  }

    tft.setCursor(105,tft.height()/2 + 20);
    tft.print(":");    
  /* Minutes */
  if(rtc_date_time.rtc_min != curr_min)
  {
    tft.fillRect(128, tft.height()/2- 40,80,70,GC9A01A_BLACK);
    if(rtc_date_time.rtc_min < 10)
    {
      tft.print(0);
      tft.print(rtc_date_time.rtc_min);
    }
    else
    {
      tft.print(rtc_date_time.rtc_min); 
    }  
    curr_min = rtc_date_time.rtc_min;
  }


  tft.setCursor(207,tft.height()/2 -20);
  /* Seconds */
  if(rtc_date_time.rtc_sec != curr_sec)
  {
    tft.setTextSize(1);
    tft.setTextColor(GC9A01A_WHITE);
    tft.fillRect(202, tft.height()/2- 40,40,30,GC9A01A_BLACK);
    if(rtc_date_time.rtc_sec < 10)
    {
      tft.print(0);
      tft.print(rtc_date_time.rtc_sec);
    }
    else
    {
      tft.print(rtc_date_time.rtc_sec); 
    }  
    curr_sec = rtc_date_time.rtc_sec;
  }
}


