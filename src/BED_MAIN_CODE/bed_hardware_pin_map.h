#ifndef BED_HARDWARE_PIN_MAP_H
#define BED_HARDWARE_PIN_MAP_H

/* Display */
static const int BED_TFT_DC       =          (uint8_t) 4;                  /* Data / Command pin for the display*/

/* I2C */
#define BED_I2C_SDA                          (uint8_t) 21                 /* SDA pin on the MCU*/
#define BED_I2C_SCL                          (uint8_t) 22                 /* SCL pin on the MCU*/


/* SPI */
static const int BED_SPI_SCK       =         (uint8_t) 18;                 /* Serial Clock pin on the MCU*/
static const int BED_SPI_MISO      =         (uint8_t) 19;                  /* Master In Slave Out pin on the MCU*/
static const int BED_SPI_MOSI      =         (uint8_t) 23;                 /* Master Out Slave In the MCU*/         
static const int BED_TFT_CS        =         (uint8_t) 2;                  /* Chip select pin for the display*/


static const int BED_SD_CS         =         (uint8_t) 14;                  /* Chip select pin for the SD Card*/

/* Sensor/IO */
#define BED_TOUCH_PAD_0                      (uint8_t) 36
#define BED_TOUCH_PAD_1                      (uint8_t) 39
#define BED_TOUCH_PAD_2                      (uint8_t) 34
#define BED_TOUCH_PAD_3                      (uint8_t) 35
#define BED_TOUCH_PAD_4                      (uint8_t) 32

const int BED_HEART_PIN            =         (uint8_t) 27;                 /* Heart Rate Pin*/

#endif