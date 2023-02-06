#ifndef BED_MPU_H
#define BED_MPU_H
uint16_t step_count = 0;
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
#endif BED_MPU_H