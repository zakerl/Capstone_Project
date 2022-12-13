// #include <bed_pedometer.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_MPU6050.h>

Adafruit_MPU6050 mpu;
float vector;
float totalvector;
float vectorprevious;
int Steps = 0;

int32_t bed_init_MPU(){ 
  
  int32_t MPU_init_error_code = BED_ERR_NONE;
  
  Wire.begin();
  Serial.begin(115200);
  while (!Serial)
    delay(10);

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");
 
  //setupt motion detection
  mpu.setHighPassFilter(MPU6050_HIGHPASS_0_63_HZ);
  mpu.setMotionDetectionThreshold(1);
  mpu.setMotionDetectionDuration(20);
  mpu.setInterruptPinLatch(true);	// Keep it latched.  Will turn off when reinitialized.
  mpu.setInterruptPinPolarity(true);
  mpu.setMotionInterrupt(true);
  delay(100);

  //Error code currently is being pressured by powerful entities to say all is well.
    if(false){
        MPU_init_error_code = BED_ERR_MPU;
    }
    return MPU_init_error_code;

}

int32_t bed_MPU_loop(){ 
  
  int32_t MPU_loop_error_code = BED_ERR_NONE;
  
  if(mpu.getMotionInterruptStatus()){
    // getAccel();
    sensors_event_t a, g, temp;
    mpu.getEvent(&a,&g,&temp);
    vector = sqrt((a.acceleration.x*a.acceleration.x) + (a.acceleration.y*a.acceleration.y) + (a.acceleration.z*a.acceleration.z));
    // Serial.print("vector:");
    // Serial.print(vector);
    // Serial.print(",");
    totalvector = vector - vectorprevious;
    // Serial.print("totalvector:");
    // Serial.print(totalvector);
    // Serial.println("");

    if (totalvector > 0.5){
      Steps++;
      Serial.print("Steps:");
      Serial.print(Steps);
      Serial.println("");
    }
    vectorprevious = vector;
    delay (100);
    // put your main code here, to run repeatedly:
    //get data from x,y,z axis
    //calculat total acceleration vector from starting point sqrt(x2+y2+z2)
    //create threshold values (through testing) to decide if a step was taken
  }
  if(false){
        MPU_loop_error_code = BED_ERR_MPU;
    }
    return MPU_loop_error_code;
}

//The average value of these 3-axis (Max + Min)/2, is called the dynamic threshold level, 
//and this threshold value is used to decide whether the step is taken or not.

//Gyro helps get rid of drift? Sensor fusion