#include "bed_display.h"

/*
    Author    : Anish Rangarajan
    Date      : 11/11/2022
    Defintion : Initializes the display system and generates team splash screen.  
*/
int32_t bed_init_display()
{
  int32_t b32_error_code = BED_ERR_NONE;
  Adafruit_SSD1306 oled(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
  Wire.begin();
  if (!oled.begin(SSD1306_SWITCHCAPVCC,SCREEN_ADDRESS))
    b32_error_code = BED_ERR_DISPLAY_SYSTEM;
    
  delay(1000);
  oled.clearDisplay();
  oled.setTextColor(WHITE);
  oled.setTextSize(TEXT_SIZE);
  oled.setCursor(0, 0);
  oled.print("BACK");
  oled.setCursor(0, 20);
  oled.print("END");
  oled.setCursor(0, 40);
  oled.print("DEVELOPERS");
  oled.display();
  return b32_error_code;
}

/*
    Author    : Anish Rangarajan
    Date      : 11/11/2022
    Defintion : Uses activity flag to generate a prompt. Saves answer to a text file.  
*/
int32_t bed_display_prompt(uint16_t bed_activity_flag)
{
  
}













































//