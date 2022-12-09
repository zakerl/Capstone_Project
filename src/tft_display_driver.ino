#include "SPI.h"
#include "Adafruit_GFX.h"
#include "Adafruit_GC9A01A.h"
#include "tft_display_driver.h"
#include "bed_prompt.h"
#include "bed_rtc.h"

int32_t bed_init_display()
{
  int32_t b32_error_code = BED_ERR_NONE;
  //b32_error_code = bed_get_i2c_status(SCREEN_ADDRESS);

  // if (!oled.begin(SSD1306_SWITCHCAPVCC,SCREEN_ADDRESS))
  // {
  //   b32_error_code = BED_ERR_DISPLAY_SYSTEM;
  //   while (1) delay(10);
  // }
  // else
  // {
    b32_error_code = BED_ERR_NONE;
    //oled.setFont(&FreeSans9pt7b);
    //delay(1000);
    bed_splash_screen(); 
  //}
  return b32_error_code;
}
void bed_splash_screen()
{
  bed_display_one_line("Back"       , 80, 80, true);
  bed_display_one_line("End"        , 90, 120, false);
  bed_display_one_line("Developers" , 30, 160, false);
  delay(1000);
}
void bed_display_one_line(char* displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag)
{
  if(clearFlag)
    tft.fillScreen(GC9A01A_BLACK);
    
  tft.setTextColor(GC9A01A_WHITE);
  tft.setCursor(coordX, coordY);
  tft.setTextSize(2);
  tft.setFont(&FreeSans9pt7b);
  tft.print(displayText);
}

void bed_display_one_line(String displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag, uint8_t textColor){
  if(clearFlag)
    tft.fillScreen(GC9A01A_BLACK);
    
  tft.setTextColor(GC9A01A_WHITE);
  tft.setCursor(coordX, coordY);
  tft.setTextSize(2);
  tft.setFont(&FreeSans9pt7b);
  tft.println(displayText);
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

void bed_display_one_line(char* displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag, uint8_t textColor, uint8_t textWrap){
  if(clearFlag)
    tft.fillScreen(GC9A01A_BLACK);
    
  tft.setTextColor(GC9A01A_WHITE);
  tft.setCursor(coordX, coordY);
  tft.setTextWrap(textWrap);
  tft.setTextSize(2);
  tft.setFont(&FreeSans9pt7b);
  tft.println(displayText);
}

void bed_display_date_time()
{

  tft.setFont(&FreeMonoBold9pt7b);
  tft.setTextColor(GC9A01A_ORANGE);
  tft.setCursor(20, 140);
  tft.setTextSize(4);
  tft.print("20");
  //tft.print(rtc_date_time.rtc_hour);
  tft.setCursor(90, 135);
  tft.print(":");
  //tft.print(rtc_date_time.rtc_min);
  tft.setCursor(110, 135);
  tft.setTextColor(GC9A01A_GREENYELLOW);
  tft.print("12");
  //tft.print(rtc_date_time.rtc_sec);
  tft.setTextSize(1);
  tft.setTextColor(GC9A01A_WHITE);
  tft.setCursor(195, 100);
  tft.print("55");


  tft.setTextSize(1);
  tft.setCursor(50, 170);
  //tft.print(rtc_date_time.rtc_year);
  tft.print("07 ");
  //tft.print(rtc_date_time.rtc_month);
  selectDay(12);
  tft.print(day);
  //tft.print(rtc_date_time.rtc_day);
  tft.print("2022 ");

}
void selectDay(uint16_t Day){
  switch(Day){
    case 1:
      sprintf(day,"%s ","Jan");
      break;
    case 2:
      sprintf(day,"%s ","Feb");
      break;
    case 3:
      sprintf(day,"%s ","Mar");
      break;
    case 4:
      sprintf(day,"%s ","Apr");
      break;
    case 5:
      sprintf(day,"%s ","May");
      break;
    case 6:
      sprintf(day,"%s ","June");
      break;
    case 7:
      sprintf(day,"%s ","July");
      break;
    case 8:
      sprintf(day,"%s ","Aug");
      break;
    case 9:
      sprintf(day,"%s ","Sept");
      break;
    case 10:
      sprintf(day,"%s ","Oct");
      break;
    case 11:
      sprintf(day,"%s ","Nov");
      break;
    case 12:
      sprintf(day,"%s ","Dec");
      break;
  }
  
}

int32_t bed_display_prompt(uint16_t bed_activity_flag)
{
  tft.fillScreen(GC9A01A_BLACK);
  char *response;
  int32_t b32_error_code = BED_ERR_NONE;
  for(int i=0; i < PROMPT_NUMBER; i++)
    {
      if (prompts[i].prompt_id == bed_activity_flag)
        {
          prompts[i].prompt_triggered = 1;
          bed_format_prompt(prompts[i].prompt_question);
          bed_display_responses();
          while (prompts[i].prompt_response == "N/A") 
          {
            selState    = digitalRead(BED_SEL_BTN);
            respState   = digitalRead(BED_RESP_BTN);  
            response    = bed_select_response(selState);
            Serial.println(response);
            if(respState == HIGH)
            {
              prompts[i].prompt_response = response;
              Serial.println(prompts[i].prompt_response);
              bed_display_one_line("Thank You", 0, 30, true);
              delay(200);
              bed_splash_screen();
              prompts[i].prompt_response = "N/A";
              return b32_error_code;
            }
          }
        }
    }

    b32_error_code = BED_ERR_INVALID_DATA;
    return b32_error_code;
}

char* bed_select_response(uint8_t buttonState)
{

  if (buttonState == HIGH) 
    buttonFlag = !buttonFlag;

  if(buttonFlag == 1)  
  {
    bed_display_one_line("___", 30, posYForLine+10, false);
    bed_display_one_line("___", 150, posYForLine+10, false, GC9A01A_BLACK);
    return "YES";
  }

  else 
  {
    bed_display_one_line("___", 150, posYForLine+10, false);
    bed_display_one_line("___", 30, posYForLine+10, false, GC9A01A_BLACK);
    return "NO";
  }
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

void bed_display_responses()
{
  tft.setTextSize(1);
  posYForLine = tft.getCursorY()+40; 
  bed_display_one_line("YES", 30, posYForLine, false);
  bed_display_one_line("NO", 150, posYForLine, false);
}

