#include "bed_errors.h"
#include <stdio.h>


void setup() 
{
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
  uint32_t b32_error_code;
  b32_error_code = bed_init_display();
  if(b32_error_code != BED_ERR_NONE)
  {
    Serial.print("Program Failed due to error:\t");
    Serial.println((int16_t)b32_error_code);
  }
  bed_display_prompt(1);
}

void loop() 
{

}