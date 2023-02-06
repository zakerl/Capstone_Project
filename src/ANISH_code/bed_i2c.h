/* Header file for useful I2C elements*/
#ifndef BED_I2C_H
#define BED_BED_I2C_H

/* Includes */
#include<Wire.h>
#include <stdint.h>

/* Definitions */
#define BAUD_RATE          57600                /* BAUD RATE for serial connection */                                                                              

/* Function Declarations */
int32_t bed_get_i2c_status(uint8_t);            /* Checks if i2c communication can be established with the device*/       


#endif 