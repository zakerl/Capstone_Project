/* Header file for the Display System*/

/* Includes*/
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "BED_ERRORS.h"

/* Definitions*/
#define SCREEN_WIDTH    128               // OLED display width, in pixels
#define TEXT_SIZE       2                 // OLED display Text size
#define SCREEN_HEIGHT   64                // OLED display height, in pixels
#define OLED_RESET      -1                // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS  0x3C              // 0x3c for current OLED module

/*Function Declarations*/
int32_t bed_init_display();
int32_t bed_display_prompt();
