#ifndef BED_HARDWARE_PIN_MAP_H
#define BED_HARDWARE_PIN_MAP_H

/* Display */
//static const int BED_TFT_RST      =          (uint8_t) 2;                 /* Reset pin # (or -1 if sharing Arduino reset pin)                                                           */
static const int BED_TFT_DC       =          (uint8_t) 3;                 /* Data / Command pin for the display*/
static const int BED_TFT_BL       =          (uint8_t) 6;                 /* Backlight pin for the display*/

/* I2C */
//#define BED_I2C_SCL                          (uint8_t) 5                  /* SCL pin on the MCU*/
//#define BED_I2C_SDA                          (uint8_t) 4                  /* SDA pin on the MCU*/

/* SPI */
static const int BED_SPI_SCK       =         (uint8_t) 8;                  /* Serial Clock pin on the MCU*/
//static const int BED_SPI_MISO      =         (uint8_t) 9;                 /* Master In Slave Out pin on the MCU*/
static const int BED_SPI_MOSI      =         (uint8_t) 10;                /* Master Out Slave In the MCU*/         
static const int BED_TFT_CS        =         (uint8_t) 7;                 /* Chip select pin for the display*/
#define BED_SD_CS                            (uint8_t) 1                  /* Chip select pin for the SD Card*/

/* Sensor/IO */
//#define BED_HEART_PIN                        (uint8_t) 0                  /* Analog pin for Heart Rate*/
#define BED_TOUCH_PAD_0                      (uint8_t) 0
#define BED_TOUCH_PAD_1                      (uint8_t) 1
#define BED_TOUCH_PAD_2                      (uint8_t) 2
#define BED_TOUCH_PAD_3                      (uint8_t) 9
#define BED_TOUCH_PAD_4                      (uint8_t) 6
#endif