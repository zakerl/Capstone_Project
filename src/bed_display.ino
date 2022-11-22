/* Implementation file for display driver*/

/*Includes*/
#include "bed_display.h"
#include "bed_prompt.h"
#include "bed_rtc.h"
/*
    Author    : Anish Rangarajan
    Date      : 11/11/2022
    Defintion : Initializes the display system.
*/
int32_t bed_init_display()
{
  int32_t b32_error_code = BED_ERR_NONE;
  b32_error_code = bed_get_i2c_status(SCREEN_ADDRESS);

  if (!oled.begin(SSD1306_SWITCHCAPVCC,SCREEN_ADDRESS))
  {
    b32_error_code = BED_ERR_DISPLAY_SYSTEM;
    while (1) delay(10);
  }
  else
  {
    b32_error_code = BED_ERR_NONE;
    oled.setFont(&FreeSans9pt7b);
    delay(1000);
    bed_splash_screen(); 
  }
  return b32_error_code;
}

/*
    Author    : Anish Rangarajan
    Date      : 11/12/2022
    Defintion : Uses activity flag to generate a prompt.  
*/
int32_t bed_display_prompt(uint16_t bed_activity_flag)
{
  oled.clearDisplay();
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

/*
    Author    : Anish Rangarajan
    Date      : 11/12/2022
    Defintion : Used to select the response for the prompt.  
*/

char* bed_select_response(uint8_t buttonState)
{

  if (buttonState == HIGH) 
    buttonFlag = !buttonFlag;

  if(buttonFlag == 1)  
  {
    bed_display_one_line("___", 10, 60, false);
    bed_display_one_line("___", 80, 60, false, BLACK);
    return "YES";
  }

  else 
  {
    bed_display_one_line("___", 80, 60, false);
    bed_display_one_line("___", 10, 60, false, BLACK);
    return "NO";
  }
}

/*
    Author    : Anish Rangarajan
    Date      : 11/12/2022
    Defintion : Formats prompt so that it can be displayed properly on the screen.  
*/
void bed_format_prompt(char *prompt_question)
{
  uint16_t prompt_len = strlen(prompt_question);
  
  char word[20];
  oled.clearDisplay();
  oled.setCursor(0, 13);
  oled.setTextColor(WHITE);
  oled.setTextWrap(true);
  for(int i=0,j=0; i <= prompt_len; i++)
  {
    if(isspace(prompt_question[i]) || prompt_question[i] == '\0' )
      {
        word[j] = '\0';
        uint16_t word_len = (strlen(word));
        if (oled.getCursorX() + word_len * CHARACTER_SIZE >= oled.width())
        {
          uint16_t remSize = (prompt_len - i + word_len)* CHARACTER_SIZE;
          oled.setCursor( (oled.width() - remSize)/2, oled.getCursorY() + 20);
        }
        oled.print(word);
        oled.print(" ");
        oled.display();
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

/*
    Author    : Anish Rangarajan
    Date      : 11/13/2022
    Defintion : Display one line of text on the given coordinates.
*/
void bed_display_one_line(char* displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag)
{
  if(clearFlag)
    oled.clearDisplay();
    
  oled.setTextColor(WHITE);
  oled.setCursor(coordX, coordY);
  oled.print(displayText);
  oled.display();
}

void bed_display_one_line(String displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag, uint8_t textColor)
{
  if(clearFlag)
    oled.clearDisplay();
    
  oled.setTextColor(textColor);
  oled.setCursor(coordX, coordY);
  oled.print(displayText);
  oled.display();
}

/*
    Author    : Anish Rangarajan
    Date      : 11/13/2022
    Defintion : Overloaded function to Display one line of text on the given coordinates with specific color.
*/
void bed_display_one_line(char* displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag, uint8_t textColor)
{
  if(clearFlag)
    oled.clearDisplay();

  oled.setTextColor(textColor);
  oled.setCursor(coordX, coordY);
  oled.print(displayText);
  oled.display();
}

/*
    Author    : Anish Rangarajan
    Date      : 11/13/2022
    Defintion : Overloaded function to Display one line of text on the given coordinates with specific color and text wrap.
*/
void bed_display_one_line(char* displayText, uint8_t coordX, uint8_t coordY, uint8_t clearFlag, uint8_t textColor, uint8_t textWrap)
{
  if(clearFlag)
    oled.clearDisplay();

  oled.setTextColor(textColor);
  oled.setCursor(coordX, coordY);
  oled.setTextWrap(textWrap);
  oled.print(displayText);
  oled.display();
}

/*
    Author    : Anish Rangarajan
    Date      : 11/12/2022
    Defintion : Scrolls provided text on the screen.  
*/
void bed_scroll_text(char* scrollText, uint8_t scrollFlag)
{
  int x, minX;
  x = oled.width();
  minX = -1 * CHARACTER_SIZE * strlen(scrollText);  // 12 = 6 pixels/character 
  
  while(scrollFlag == true)
  {
    oled.clearDisplay();
    oled.setCursor(x, 30);
    oled.setTextWrap(false);
    oled.print(scrollText);
    oled.display();
    x=x-3; // scroll speed, make more positive to slow down the scroll

    if(x < minX)
      {
        bed_format_prompt(scrollText);
        break;
      }
  }
}

/*
    Author    : Anish Rangarajan
    Date      : 11/11/2022
    Defintion : Generates team splash screen.  
*/
void bed_splash_screen()
{
  bed_display_one_line("Back"       , 0, 20, true);
  bed_display_one_line("End"        , 0, 40, false);
  bed_display_one_line("Developers" , 0, 60, false);
  delay(1000);
}

/*
    Author    : Anish Rangarajan
    Date      : 11/12/2022
    Defintion : Displays possible responses on the screen.  
*/
void bed_display_responses()
{
  bed_display_one_line("YES", 10, 58, false);
  bed_display_one_line("NO", 80, 58, false);
}

/*
    Author    : Anish Rangarajan
    Date      : 11/19/2022
    Defintion : Displays Date and Time.  
*/
void bed_display_date_time()
{
  oled.fillRect(0, 0, 128, 25, WHITE);
  oled.fillRect(0, 35, 128, 25, WHITE);

  oled.setTextColor(BLACK);
  oled.setCursor(20, 20);
  oled.print(rtc_date_time.rtc_year);
  oled.print(":");
  oled.print(rtc_date_time.rtc_month);
  oled.print(":");
  oled.print(rtc_date_time.rtc_day);

  oled.setCursor(20, 55);
  oled.print(rtc_date_time.rtc_hour);
  oled.print(":");
  oled.print(rtc_date_time.rtc_min);
  oled.print(":");
  oled.print(rtc_date_time.rtc_sec);

  oled.display();

}



















































//