/* Header file for the Pedometer system*/

/* Includes*/
#include <Wire.h>
#include <Adafruit_Sensor.h>
// #include <Adafruit_ADXL343.h>
#include <Adafruit_MPU6050.h>
//#include "BED_ERRORS.h"

/* Definitions*/

// #define ADXL343_SCK 13        //pin defintions
// #define ADXL343_MISO 12
// #define ADXL343_MOSI 11
// #define ADXL343_CS 10        

/* Global Declarations*/
//Declaration for ADXL object
Adafruit_MPU6050 mpu; //mpu object


/*Function Declarations*/
// void    bed_splash_screen();
// int32_t bed_init_display();
// int32_t bed_display_prompt();