#include <stdio.h>
#include "bed_errors.h"

// int sensorPin = 0;

void setup() {
    Serial.begin(9600);
    uint32_t HR_error_code;
    HR_error_code = bed_init_HR();
    if(HR_error_code != BED_ERR_NONE)
    {
        Serial.print("Program Failed due to heart rate init error:\t");
        Serial.println((int16_t)HR_error_code);
    }
    HR_error_code = bed_HR_serial_plot();
    if(HR_error_code != BED_ERR_NONE)
    {
        Serial.print("Program Failed due to heart rate loop error:\t");
        Serial.println((int16_t)HR_error_code);
    }
}

void loop (){
  
}