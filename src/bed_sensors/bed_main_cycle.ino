#include <stdio.h>
#include "bed_errors.h"

// int sensorPin = 0;
uint32_t HR_error_code;
uint32_t MPU_error_code;

void setup () {
    Serial.begin(9600);

    // Initialize Heart Rate Module
    HR_error_code = bed_init_HR();
    if(HR_error_code != BED_ERR_NONE)
    {
        Serial.print("Program Failed due to heart rate init error:\t");
        Serial.println((int16_t)HR_error_code);
    }

    // Initialize MPU Module
    MPU_error_code = bed_init_MPU();
    if(MPU_error_code != BED_ERR_NONE)
    {
        Serial.print("Program Failed due to MPU init error:\t");
        Serial.println((int16_t)MPU_error_code);
    }

}

void loop (){

    // Run Heart Rate Sensor
    HR_error_code = bed_HR_loop();
    if(HR_error_code != BED_ERR_NONE)
    {
        Serial.print("Program Failed due to heart rate loop error:\t");
        Serial.println((int16_t)HR_error_code);
    }
    // Run MPU sensor
    MPU_error_code = bed_MPU_loop();
    if(MPU_error_code != BED_ERR_NONE)
    {
        Serial.print("Program Failed due to MPU loop error:\t");
        Serial.println((int16_t)MPU_error_code);
    }
}