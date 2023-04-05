//Code should count the number of steps based on how many flags are tripped.
//Making some type of calibration so this works on other MPU sensors would be a good idea.
//For now, 2 of accx,accy,accz need to go 2 values away from baseline. 
//First, get a baseline reading of the sensors 4 seconds after the code boots up, store those averages into variables
//Second, continually obtain sensor readings in a infinite loop and check flags against baseline values.
//If enough flags are tripped, within a 2 second time period, count up. If 2 seconds passes, reset all flags. 

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include "bed_mpu.h"
#include "bed_errors.h"

Adafruit_MPU6050 mpu;

/* 
  Initializes the MPU.
  Params : N/A
  Outputs: Error Code.
*/
int32_t bed_MPU_setup() 
{
  if (!mpu.begin(MPU_ADDR)) 
  {
    Serial.println("Failed to find MPU6050 chip");
    return BED_ERR_MPU;
  }

  Serial.println("MPU6050 Found!");

  //setting MPU parameters
  mpu.setAccelerometerRange(MPU6050_RANGE_2_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  for(int i=0;i<10;i++)
  {
      sensors_event_t a, g, temp;
      mpu.getEvent(&a, &g, &temp); 
      // init_ax[init_count] = a.acceleration.x;  
      sum_ax = sum_ax + a.acceleration.x;
      sum_ay = sum_ay + a.acceleration.y;
      sum_az = sum_az + a.acceleration.z;
  }

  avg_ax = sum_ax / 10;
  avg_ay = sum_ay / 10;
  avg_az = sum_az / 10;

  Serial.print("avg X acc: ");
  Serial.print(avg_ax);
  Serial.print(", avg Y acc: ");
  Serial.print(avg_ay);
  Serial.print(", avg Z acc: ");
  Serial.println(avg_az);

  return BED_ERR_NONE;

}

/* 
  Detects footsteps and detects when an activity occurs.
  Params : currentTime: Current cycle of the program.
  Outputs: Error Code.
*/
int32_t bed_MPU_detect(unsigned long currentTime)
 {
     

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp); 

    curr_ax = a.acceleration.x;
    curr_ay = a.acceleration.y;
    curr_az = a.acceleration.z;
    curr_gx = g.gyro.x;
    curr_gy = g.gyro.y;
    curr_gz = g.gyro.z;
      

    
    if (curr_ax > avg_ax+ACCEL_SENSITIVITY || avg_ax-ACCEL_SENSITIVITY > curr_ax)
    {
      flag_ax = 1;
    }
    if (curr_ay > avg_ay+ACCEL_SENSITIVITY || avg_ay-ACCEL_SENSITIVITY > curr_ay) {
      flag_ay = 1;
    }
    if (curr_az > avg_az+ACCEL_SENSITIVITY || avg_az-ACCEL_SENSITIVITY > curr_az) {
      flag_ax = 1;
    }
    if (curr_gx > GYRO_SENSITIVITY || -GYRO_SENSITIVITY > curr_gx) {
      flag_gx = 1;
    }
    if (curr_gy > GYRO_SENSITIVITY || -GYRO_SENSITIVITY > curr_gy) {
      flag_gy = 1;
    }
    if (curr_gz > GYRO_SENSITIVITY || -GYRO_SENSITIVITY > curr_gz) {
      flag_gz = 1;
    }

    sum_of_flags = flag_ax + flag_ay + flag_az + flag_gx + flag_gy + flag_gz;
    
    if (sum_of_flags >= 4) {
      TOTAL_STEP += 1;
      step_count += 1;
      activity_timeout = currentTime;
      stepResetTime = currentTime;
      step_flag = 1;
      // Reset activity timer
      
      Serial.print("stepcount: ");
      Serial.println(step_count);
      
      flag_ax = 0;
      flag_ay = 0;
      flag_az = 0;
      flag_gx = 0;
      flag_gy = 0;
      flag_gz = 0;

    }

    if (flag_reset_count >= 8) { //approx 2 seconds.
      flag_reset_count = 0;
      flag_ax = 0;
      flag_ay = 0;
      flag_az = 0;
      flag_gx = 0;
      flag_gy = 0;
      flag_gz = 0;
    }

    flag_reset_count++;

  if(step_count >= ACTIVITY_STEPS)
  {
    activity_flag = 1;
  }
  
  if(activity_flag && (currentTime - activity_timeout > ACTIVITY_IDLE_WAIT))
  {
    activity_pauses += 1;
    Serial.println("Activity");
    activity_timeout = currentTime;
    stepResetTime = currentTime;

    activity_flag = 0;
    step_count = 0;
    step_flag = 0;
    
    changeState(KEY_4_INPUT);
  }

  if(step_flag && (currentTime - stepResetTime > ACTIVITY_IDLE_RESET))
  {
    Serial.println("Idle");
    step_count = 0;
    step_flag = 0;
    stepResetTime = currentTime;  
  }
  
  
  
return 0;
}