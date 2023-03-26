#include <stdint.h>
#include "WString.h"
/* Header file for the Display System*/
#ifndef BED_TFT_DISPLAY_H
#define BED_TFT_DISPLAY_H

/* Includes*/
#include <Adafruit_GFX.h>
#include <Adafruit_GC9A01A.h>
#include "bed_errors.h"
#include <Fonts/FreeSans9pt7b.h>
#include "bed_hardware_pin_map.h"
#include <string.h>

/* Definitions*/
#define TEXT_SIZE               1                                                             /* TFT display Text size                                                                                      */
#define SCREEN_ADDRESS          0x3C                                                          /* 0x3c for current OLED module                                                                               */
#define PIXELS_PER_CHARACTER    20                                                            /* Amount of pixels taken up by each character                                                                */
#define CHARACTER_SIZE          TEXT_SIZE * PIXELS_PER_CHARACTER                              /* Size of each character in pixels                                                                           */
#define CURSOR_WIDTH            10
#define CURSOR_HEIGHT           10

/* Global Declarations*/

/* Global declaration of the tft object */

Adafruit_GC9A01A tft(BED_TFT_CS, BED_TFT_DC, BED_SPI_MOSI, BED_SPI_SCK);
uint8_t promptState = 0;
uint8_t buttonFlag  = 0;                                                                      /* Flag variable linked with button state                                                                     */
uint8_t dateScreenFlag  = 0;                                                                  /* Flag variable linked with date screen                                                                      */
uint8_t posYForLineInt = 0;                                                                   /* Intended Position Y for placing line for selected option                                                   */
uint8_t posYForLine = 0;                                                                      /* Position Y for placing line for selected option                                                            */
int8_t  scroll_index = -1;
uint8_t draw_flag = 0;

/*Function Declarations*/         
int32_t bed_init_display();                                                                   /* Initializes the display system.                                                                            */                            
//int32_t bed_display_prompt();                                                               /* Uses activity flag to generate a prompt. Saves answer to a text file.                                      */
//void    bed_format_prompt(char*);                                                           /* Formats prompt so that it can be displayed properly on the screen.                                         */   
void    bed_display_one_line(char*, uint8_t, uint8_t, uint8_t);                               /* Display one line of text on the given coordinates                                                          */  
void    bed_display_one_line(String, uint8_t, uint8_t, uint8_t, uint8_t);                     /* Display one line of text on the given coordinates                                                          */  
void    bed_display_one_line(char*, uint8_t, uint8_t, uint8_t, uint8_t);                      /* Overloaded function to Display one line of text on the given coordinates with specific color               */
void    bed_display_one_line(char*, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t);             /* Overloaded function to Display one line of text on the given coordinates with specific color and text wrap */
void    bed_scroll_text(char*, uint8_t);                                                      /* Generates team splash screen                                                                               */
void    bed_splash_screen();                                                                  /* Scrolls provided text on the screen                                                                        */
void    bed_display_prompt(int8_t ,uint8_t, uint8_t, uint8_t);                                /* Scrolls provided text on the screen                                                                        */
void    bed_display_date_time();                                                              /* Displays Date and Time                                                                                     */
//void    bed_select_day(uint16_t currDay);                                                   /* Filters out corresponding month                                                                            */

#endif
























//