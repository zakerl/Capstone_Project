#include <stdint.h>
#include "WString.h"
/* Header file for the Display System*/
#ifndef BED_DISPLAY_H
#define BED_DISPLAY_H

/* Includes*/
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "bed_errors.h"
#include <Fonts/FreeSans9pt7b.h>
#include "bed_hardware_pin_map.h"
#include <string.h>

/* Definitions*/
#define SCREEN_WIDTH            128                                                           /* OLED display width, in pixels                                                                              */
#define TEXT_SIZE               1                                                             /* OLED display Text size                                                                                     */
#define SCREEN_HEIGHT           64                                                            /* OLED display height, in pixels                                                                             */
#define OLED_RESET              -1                                                            /* Reset pin # (or -1 if sharing Arduino reset pin)                                                           */
#define SCREEN_ADDRESS          0x3C                                                          /* 0x3c for current OLED module                                                                               */
#define PIXELS_PER_CHARACTER    9                                                             /* Amount of pixels taken up by each character                                                                */
#define CHARACTER_SIZE          TEXT_SIZE * PIXELS_PER_CHARACTER                              /* Size of each character in pixels                                                                           */

/* Global Declarations*/
Adafruit_SSD1306 oled(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
uint8_t selState    = 0;                                                                      /* Current State of the select button                                                                         */
uint8_t respState   = 0;                                                                      /* Current State of the response button                                                                       */
uint8_t buttonFlag  = 0;                                                                      /* Flag variable linked with button state                                                                     */

/*Function Declarations*/         
int32_t bed_init_display();                                                                   /* Initializes the display system.                                                                            */                            
int32_t bed_display_prompt();                                                                 /* Uses activity flag to generate a prompt. Saves answer to a text file.                                      */
char*   bed_select_response(uint8_t);                                                         /* Used to select the response for the prompt.                                                                */
void    bed_format_prompt(char*);                                                             /* Formats prompt so that it can be displayed properly on the screen.                                         */   
void    bed_display_one_line(char*, uint8_t, uint8_t, uint8_t);                               /* Display one line of text on the given coordinates                                                          */  
void    bed_display_one_line(String, uint8_t, uint8_t, uint8_t, uint8_t);                     /* Display one line of text on the given coordinates                                                          */  
void    bed_display_one_line(char*, uint8_t, uint8_t, uint8_t, uint8_t);                      /* Overloaded function to Display one line of text on the given coordinates with specific color               */
void    bed_display_one_line(char*, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t);             /* Overloaded function to Display one line of text on the given coordinates with specific color and text wrap */
void    bed_scroll_text(char*, uint8_t);                                                      /* Generates team splash screen                                                                               */
void    bed_splash_screen();                                                                  /* Scrolls provided text on the screen                                                                        */
void    bed_display_responses();                                                              /* Displays possible responses on the screen                                                                  */
void    bed_display_date_time();                                                              /* Displays Date and Time                                                                                     */


#endif
























//