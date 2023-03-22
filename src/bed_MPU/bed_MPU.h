#ifndef BED_MPU_H
#define BED_MPU_H

#define MPU_EVENT 400
#define MPU_CALIBRATION 4000
#define NO_ACTIVITY_TIME 60000
// Tracks the total number of steps over the course of the EMA period.
uint16_t TOTAL_STEP = 0;

// Tracks the number of steps currently in the activity
uint16_t step_count = 0;

// This is a timer. When this value hits a high enough value, activity_step is reset to zero. If activity step is higher than a certain threshold, then the relevant prompt is generated.
uint16_t activity_timeout = 0;

uint16_t init_count = 0;
uint16_t flag_reset_count=0;
uint16_t limp_count = 0;


// Step flags
uint8_t flag_ax = 0;
uint8_t flag_ay = 0;
uint8_t flag_az = 0; 
uint8_t flag_gz = 0;
uint8_t flag_gy = 0; 
uint8_t flag_gx = 0;
uint8_t sum_of_flags;

// Limp flags
uint8_t limp_flag_ax = 0;
uint8_t limp_flag_ay = 0;
uint8_t limp_flag_az = 0; 
uint8_t limp_flag_gz = 0;
uint8_t limp_flag_gy = 0; 
uint8_t limp_flag_gx = 0;
uint8_t sum_of_limp_flags;

// Step helper variables
float sum_ax, sum_ay, sum_az;
float avg_ax, avg_ay, avg_az; 
float curr_ax, curr_ay, curr_az, curr_gx, curr_gy, curr_gz;

unsigned long MPULooptime = 0;
unsigned long MPUSetuptime = 0;
unsigned long stepResetTime = 0;
#endif BED_MPU_H