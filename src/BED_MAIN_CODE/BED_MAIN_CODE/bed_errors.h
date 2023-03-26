 /* Header file for the Error Codes used in the system */
#ifndef BED_ERRORS_H
#define BED_ERRORS_H

#define BED_ERR_NONE                        (int32_t)    0       /*No error*/
#define BED_ERR_I2C_CONNECTION              (int32_t)   -1       /*I2C connection error*/
#define BED_ERR_INVALID_DATA                (int32_t)   -2       /*Invalid data error*/
#define BED_ERR_INVALID_DATA_SIZE           (int32_t)   -3       /*Invalid data size error*/
#define BED_ERR_DISPLAY_SYSTEM              (int32_t)   -4       /*Display system not working error*/
#define BED_ERR_RTC_SYSTEM                  (int32_t)   -5       /*RTC system not working error*/
#define BED_ERR_HR_SYSTEM                   (int32_t)   -6       /**/  

#endif