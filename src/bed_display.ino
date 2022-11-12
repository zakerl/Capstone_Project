/*Includes*/
#include "bed_display.h"
#include "bed_prompt.h"
/*
    Author    : Anish Rangarajan
    Date      : 11/11/2022
    Defintion : Initializes the display system  
*/
int32_t bed_init_display()
{
  oled.setFont(&FreeSans9pt7b);
  int32_t b32_error_code = BED_ERR_NONE;
  
  Wire.begin();
  if (!oled.begin(SSD1306_SWITCHCAPVCC,SCREEN_ADDRESS))
    b32_error_code = BED_ERR_DISPLAY_SYSTEM;
    
  delay(1000);
  bed_splash_screen();
  return b32_error_code;
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
  minX = -6 * TEXT_SIZE * strlen(scrollText);  // 12 = 6 pixels/character 
  
  while(scrollFlag == true)
  {
    oled.clearDisplay();
    oled.setCursor(x, 30);
    oled.setTextWrap(false);
    oled.println(scrollText);
    oled.display();
    x=x-3; // scroll speed, make more positive to slow down the scroll
    if(x < minX)
      {
        oled.clearDisplay();
        oled.setTextSize(TEXT_SIZE);
        oled.setCursor(0, 20);
        oled.setTextWrap(true);
        oled.print(scrollText);
        oled.display();
        break;
      }
  }
}
/*
    Author    : Anish Rangarajan
    Date      : 11/12/2022
    Defintion : Displays possible responses on the screen  
*/
void bed_display_responses()
{
  oled.setCursor(10, 50);
  oled.print("YES");
  oled.setCursor(80, 50);
  oled.print("NO");
  oled.display();
}

/*
    Author    : Anish Rangarajan
    Date      : 11/11/2022
    Defintion : Generates team splash screen.  
*/
void bed_splash_screen()
{
  
  oled.clearDisplay();
  oled.setTextColor(WHITE);
  oled.setTextSize(TEXT_SIZE);
  oled.setCursor(0, 20);
  oled.print("BACK");
  oled.setCursor(0, 40);
  oled.print("END");
  oled.setCursor(0, 60);
  oled.print("DEVELOPERS");
  oled.display();
  delay(1000);
}

/*
    Author    : Anish Rangarajan
    Date      : 11/12/2022
    Defintion : Used to select the response for the prompt.  
*/

void bed_select_response(int buttonState)
{

  if (buttonState == HIGH) 
    buttonFlag = !buttonFlag;

  if(buttonFlag == 1)  
  {
    oled.setTextColor(WHITE);
    oled.setCursor(10, 55);
    oled.print("___");
    
    oled.setTextColor(BLACK);
    oled.setCursor(80, 55);
    oled.print("___");
    oled.display();
  }
  else 
  {
    oled.setTextColor(WHITE);
    oled.setCursor(80, 55);
    oled.print("___");
    
    oled.setTextColor(BLACK);
    oled.setCursor(10, 55);
    oled.print("___");
    oled.display();
  }
  
  

}

/*
    Author    : Anish Rangarajan
    Date      : 11/12/2022
    Defintion : Uses activity flag to generate a prompt. Saves answer to a text file.  
*/
int32_t bed_display_prompt(uint16_t bed_activity_flag)
{

  
  int32_t b32_error_code = BED_ERR_NONE;
  for(int i=0; i < PROMPT_NUMBER; i++)
    {
      if (prompts[i].prompt_id == bed_activity_flag)
        {
          prompts[i].prompt_triggered = 1;
          bed_scroll_text(prompts[i].prompt_question,true);
          bed_display_responses();
          while(prompts[i].prompt_response == "N/A")
          {
            buttonState = digitalRead(buttonPin);
            Serial.println(buttonState);
            bed_select_response(buttonState);
            delay(100);
          }
        }
    }
}













































//