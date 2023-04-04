//Code should count the number of steps based on how many flags are tripped.
//Making some type of calibration so this works on other MPU sensors would be a good idea.
//For now, 2 of accx,accy,accz need to go 2 values away from baseline. 
//First, get a baseline reading of the sensors 4 seconds after the code boots up, store those averages into variables
//Second, continually obtain sensor readings in a infinite loop and check flags against baseline values.
//If enough flags are tripped, within a 2 second time period, count up. If 2 seconds passes, reset all flags. 

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include "bed_MPU.h"

Adafruit_MPU6050 mpu;

void setup(void){
  bed_MPU_setup();
}

void loop(void){
  bed_MPU_detect();
}

int32_t bed_MPU_setup() {
  Serial.begin(19200);
  // Try to initialize
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    return -5;
  }
  Serial.println("MPU6050 Found!");

  //setting MPU parameters
  mpu.setAccelerometerRange(MPU6050_RANGE_2_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  Serial.println("Calibrating MPU in 4 seconds! Hold it still!");
  unsigned long currentTime = millis(); // Gets the current time
  if(currentTime - MPUSetuptime >= MPU_CALIBRATION){
  //baseline readings for acceleration (gyro is assumed to be 0)
  //can we notify the user to "hold device still while calibrating" on boot. Might have change this message to "hold device to your side" or something.
  while (init_count < 10){  //count 10 times with 100 millisec. delay of 4 seconds (above). 
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp); 
    // init_ax[init_count] = a.acceleration.x;  
    sum_ax = sum_ax + a.acceleration.x;
    sum_ay = sum_ay + a.acceleration.y;
    sum_az = sum_az + a.acceleration.z;
    init_count++;
  }
  avg_ax = sum_ax / init_count;
  avg_ay = sum_ay / init_count;
  avg_az = sum_az / init_count;
  Serial.print("avg X acc: ");
  Serial.print(avg_ax);
  Serial.print(", avg Y acc: ");
  Serial.print(avg_ay);
  Serial.print(", avg Z acc: ");
  Serial.println(avg_az);
  MPUSetuptime = currentTime;

  return 0;
}
}

int32_t bed_MPU_detect() {
  unsigned long currentTime = millis(); // Gets the current time
  if(currentTime - MPULooptime >= MPU_EVENT){
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp); 

    curr_ax = a.acceleration.x;
    curr_ay = a.acceleration.y;
    curr_az = a.acceleration.z;
    curr_gx = g.gyro.x;
    curr_gy = g.gyro.y;
    curr_gz = g.gyro.z;
      
    //  Serial.println("Raw Accel Values ");
    //  Serial.print("Ax: ");
    //  Serial.println(curr_ax);
    //
    //  Serial.print("Ay: ");
    //  Serial.println(curr_ay);
    //
    //  Serial.print("Az: ");
    //  Serial.println(curr_az);
    //
    //  Serial.print("Gx: ");
    //  Serial.println(curr_gx);
    //
    //  Serial.print("Gy: ");
    //  Serial.println(curr_gy);
    //
    //  Serial.print("Gz: ");
    //  Serial.println(curr_gz);
    
    if (curr_ax > avg_ax+ACCEL_SENSITIVITY || avg_ax-ACCEL_SENSITIVITY > curr_ax) {
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
    
    //Limp flag ifs, changed the thresholds off experimental data.
    if (avg_ax-7 > curr_ax) {
    limp_flag_ax = 1;
    }
    if (curr_az > avg_az+2 || avg_az-2 > curr_az) {
      limp_flag_az = 1;
    }
    if ((curr_gz < 1 && curr_gz > 0.5)|| (-1 < curr_gz && -0.5 > curr_gz)) {
      limp_flag_gz = 1;
    }
    // Register a limp event
    if(limp_flag_az && limp_flag_ax && limp_flag_gz){
      Serial.println("limp count +");
      limp_count += 1;
      limp_flag_gz = 0;
      limp_flag_az = 0;
      limp_flag_ax = 0;
      }

    if(limp_count >= 3){
      limp_count = 0;
      Serial.println("limping. ");
      // input = 2; //Set state to 2
    }

    sum_of_flags = flag_ax + flag_ay + flag_az + flag_gx + flag_gy + flag_gz;
    
    if (sum_of_flags >= 4) {
      TOTAL_STEP += 1;
      step_count += 1;
      // Reset activity timer
      
      activity_timeout = currentTime;
      
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
    MPULooptime = currentTime;
  }
  if(step_count >= 30){
    activity_flag = 1;
  }
  if(activity_flag && (currentTime - activity_timeout > FIVE_SECONDS)){
    //pause, ask why when activity ends?
    activity_pauses += 1;
    Serial.println("activity pauses:");
    Serial.println(activity_pauses);
    activity_timeout = currentTime;
  }
  if(activity_flag && (currentTime - activity_timeout > THIRTY_SECONDS)){
    //prompt end of activity
    step_count = 0;
    Serial.println("why stop?");
    activity_flag = 0;
    activity_timeout = currentTime;  
  }
  
  
  
return 0;
}