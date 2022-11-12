/* Header file for the Display System*/

/* Includes*/
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "BED_ERRORS.h"
#include <Fonts/FreeSans9pt7b.h>
/* Definitions*/
#define SCREEN_WIDTH    128               // OLED display width, in pixels
#define TEXT_SIZE       1                 // OLED display Text size
#define SCREEN_HEIGHT   64                // OLED display height, in pixels
#define OLED_RESET      -1                // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS  0x3C              // 0x3c for current OLED module

/* Global Declarations*/
Adafruit_SSD1306 oled(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
uint8_t buttonPin = 6;
uint8_t buttonState = 0;
uint8_t buttonFlag = 0;
/*Function Declarations*/
void    bed_splash_screen();
int32_t bed_init_display();
int32_t bed_display_prompt();
