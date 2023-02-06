#include "SPI.h"
#include "Adafruit_GFX.h"
#include "Adafruit_GC9A01A.h"
#include "bed_display.h"
#include "bed_prompt.h"
#include "bed_rtc.h"

uint8_t curr_hr = 0, curr_min = 0, curr_sec = 0;
char final[MAX_PROMPTS][20];
int32_t bed_init_display()
{
  int32_t b32_error_code = BED_ERR_NONE;
  /* Add display startup check code here*/
  tft.begin();
  tft.setRotation(4);
  bed_splash_screen(); 
  tft.fillScreen(GC9A01A_BLACK);
  return b32_error_code;
}


void bed_scroll_test(int8_t direction, uint8_t no_of_options, uint8_t flag)
{
  tft.setTextSize(1);
  uint8_t cursorPosX[2] = {110, 90};
  uint8_t cursorPosY[no_of_options];
  char options[50];
  uint16_t offset = tft.height()/no_of_options;
  for( uint8_t i=0,j=1; i < no_of_options && j<= no_of_options; i++,j++)
  {
    cursorPosY[i] = j*offset  - 20 ;
    if(!flag)
      sprintf(options,"%d",j);

    else if(flag == 1)
    {
      sprintf(options,"%s",final[i]);      
    }
    bed_display_one_line(options, cursorPosX[0]  , cursorPosY[i], false);
  }

  if(direction == 5)
  {
    Serial.println(final[scroll_index]);
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

void bed_splash_screen()
{
  tft.setTextSize(2);
  bed_display_one_line("Back"       , tft.width()/7.5, tft.height()/3 + 10, false);
  bed_display_one_line("End"        , tft.width()/7.5, tft.height()/2 + 10, false);
  bed_display_one_line("Developers" , tft.width()/7.5, tft.height()/1.5 + 10, false);
  
  yield();
}

void bed_display_one_line(char* displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag)
{
  if(clearFlag)
    tft.fillScreen(GC9A01A_BLACK);
    
  tft.setTextColor(GC9A01A_WHITE);
  tft.setCursor(coordX, coordY);
  tft.setFont(&FreeSans9pt7b);
  tft.print(displayText);

}

void bed_display_one_line(char* displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag, uint8_t textColor){
  if(clearFlag)
    tft.fillScreen(GC9A01A_BLACK);
    
  tft.setTextColor(GC9A01A_WHITE);
  tft.setCursor(coordX, coordY);
  tft.setTextSize(2);
  tft.setFont(&FreeSans9pt7b);
  tft.println(displayText);
}


void bed_display_date_time()
{
  char hour[2];
  if(rtc_date_time.rtc_hour <10)
      sprintf(hour,"0%d",rtc_date_time.rtc_hour);
  else  
      sprintf(hour,"%d",rtc_date_time.rtc_hour);

  char min[2];
  if(rtc_date_time.rtc_min <10)
      sprintf(min,"0%d",rtc_date_time.rtc_min);
  else  
      sprintf(min,"%d",rtc_date_time.rtc_min);

  char sec[2];
  if(rtc_date_time.rtc_sec <10)
      sprintf(sec,"0%d",rtc_date_time.rtc_sec);
  else  
      sprintf(sec,"%d",rtc_date_time.rtc_sec);

      
  
  tft.setFont(&FreeSans9pt7b);

  tft.setTextColor(GC9A01A_ORANGE);
  tft.setCursor(20, 140);
  tft.setTextSize(4);
  
  if(curr_hr != rtc_date_time.rtc_hour)
  {
    tft.fillRect(28, 80,70,70,GC9A01A_BLACK);
    yield();
    tft.print(hour);
    curr_hr = rtc_date_time.rtc_hour;
  }
  else
  {
    tft.print(hour);
    curr_hr = rtc_date_time.rtc_hour;
  }

  
  tft.setCursor(98, 135);
  tft.print(":");

  tft.setCursor(110, 140);
  tft.setTextColor(GC9A01A_GREENYELLOW);

  if(curr_min != rtc_date_time.rtc_min)
  {
    tft.fillRect(114, 80,76,70,GC9A01A_BLACK);
    yield();
    tft.print(min);
    curr_min = rtc_date_time.rtc_min;
  }
  else
  {
    tft.print(min);
    curr_min = rtc_date_time.rtc_min;
  }
 
  tft.setTextSize(1);
  tft.setTextColor(GC9A01A_WHITE);
  tft.setCursor(195, 100);
  
  if(curr_sec != rtc_date_time.rtc_sec)
  {
    tft.fillRect(193, 80,30,25,GC9A01A_BLACK);
    yield();
    tft.print(sec);
    curr_sec = rtc_date_time.rtc_sec;
  }
  
  else 
  {
    tft.print(sec);
    curr_sec = rtc_date_time.rtc_sec;
  }

  tft.setTextSize(1);
  tft.setCursor(50, 170);

  //tft.print(rtc_date_time.rtc_year);
  tft.print("07 ");
  //tft.print(rtc_date_time.rtc_month);
  //bed_select_day(12);
  //tft.print(day);
  //tft.print(rtc_date_time.rtc_day);
  tft.print("2022 ");

}


int32_t bed_display_prompt(int8_t direction, uint8_t prompt_index)
{
  char subtext[20];
  

   char str[80];
   char buff[80];
   strcpy(str,prompt_walking[prompt_index].prompt_possible_answers );
   const char s[2] = "-";
   char *token;
   
   /* get the first token */
   token = strtok(str, s);
   int i=0;
   /* walk through other tokens */
   while( token != NULL ) {
      sprintf( buff,"%s\n", token );
      strcpy(final[i],buff);
      
      token = strtok(NULL, s);
      i++;
   }
  
   bed_scroll_test(direction, prompt_walking[prompt_index].no_of_options, 1);
  
}


void bed_format_prompt(char *prompt_question)
{
  uint16_t prompt_len = strlen(prompt_question);
  
  char word[20];
  tft.fillScreen(GC9A01A_BLACK);
  tft.setCursor(15, 80);
  tft.setTextWrap(true);
   tft.setTextColor(GC9A01A_WHITE);
  tft.setTextSize(2);
  tft.setFont(&FreeSans9pt7b);
  for(int i=0,j=0; i <= prompt_len; i++)
  {
    if(isspace(prompt_question[i]) || prompt_question[i] == '\0' )
      {
        word[j] = '\0';
        uint16_t word_len = (strlen(word));
        if (tft.getCursorX() + word_len * CHARACTER_SIZE >= tft.width())
        {
          uint16_t remSize = (prompt_len - i + word_len)* CHARACTER_SIZE;
          tft.setCursor( (tft.width() - remSize)/2, tft.getCursorY() + 30);
        }
        tft.print(word);
        tft.print(" ");
        strcpy(word, "");
        j=0;
      }
    else 
    {
      word[j] = prompt_question[i];
      j++;
    }
  }
}


