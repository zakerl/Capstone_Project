//Code should count the number of steps based on how many flags are tripped.
//Making some type of calibration so this works on other MPU sensors would be a good idea.
//For now, 2 of accx,accy,accz need to go 2 values away from baseline. 
//First, get a baseline reading of the sensors 4 seconds after the code boots up, store those averages into variables
//Second, continually obtain sensor readings in a infinite loop and check flags against baseline values.
//If enough flags are tripped, within a 2 second time period, count up. If 2 seconds passes, reset all flags. 

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

int step_count = 0;
int count = 0; 
int init_count = 0;
int flag_reset_count=0;

int flag_ax = 0;
int flag_ay = 0;
int flag_az = 0; 
int flag_gz = 0;
int flag_gy = 0; 
int flag_gx = 0;
int sum_of_flags;

float sum_ax, sum_ay, sum_az;
float avg_ax, avg_ay, avg_az; 
float curr_ax, curr_ay, curr_az, curr_gx, curr_gy, curr_gz;

Adafruit_MPU6050 mpu;

void setup(void) {
	Serial.begin(19200);

	// Try to initialize
	if (!mpu.begin()) {
		Serial.println("Failed to find MPU6050 chip");
		while (1) {
		  delay(10);
		}
	}
	Serial.println("MPU6050 Found!");

	//setting MPU parameters
  mpu.setAccelerometerRange(MPU6050_RANGE_2_G);
	mpu.setGyroRange(MPU6050_RANGE_500_DEG);
	mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  Serial.println("Calibrating MPU in 4 seconds! Hold it still!");
	delay(4000);

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

}

void loop() {
  
	while (1) { 
  sensors_event_t a, g, temp;
	mpu.getEvent(&a, &g, &temp); 

	curr_ax = a.acceleration.x;
  curr_ay = a.acceleration.y;
  curr_az = a.acceleration.z;
  curr_gx = g.gyro.x;
  curr_gy = g.gyro.y;
  curr_gz = g.gyro.z;
	
  if (curr_ax > avg_ax+2 || avg_ax-2 > curr_ax) {
    flag_ax = 1;
  }
  if (curr_ay > avg_ay+2 || avg_ay-2 > curr_ay) {
    flag_ay = 1;
  }
  if (curr_az > avg_az+2 || avg_az-2 > curr_az) {
    flag_ax = 1;
  }
  if (curr_gx > 1 || -1 > curr_gx) {
    flag_gx = 1;
  }
  if (curr_gy > 1 || -1 > curr_gy) {
    flag_gy = 1;
  }
  if (curr_gz > 1 || -1 > curr_gz) {
    flag_gz = 1;
  }

  sum_of_flags = flag_ax + flag_ay + flag_az + flag_gx + flag_gy + flag_gz;

  if (sum_of_flags >= 4) {
    step_count += 1;
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
  // count++;
  
	delay(400); 
  
  }
}