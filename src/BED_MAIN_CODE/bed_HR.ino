#include "bed_HR.h"
PulseSensorPlayground pulseSensor;  /* Creates an object */
int Signal; 

/* 
  Sets up the Heart Rate Sensor.
  Params : N/A
  Outputs: N/A
*/
void bed_HR_setup() {
  /* Configure the PulseSensor object, by assigning our variables to it */
  pulseSensor.analogInput(BED_HEART_PIN);   
  pulseSensor.setThreshold(Threshold);   

  /* Double-check the "pulseSensor" object was created and began seeing a signal */
  if (pulseSensor.begin()) {
    Serial.println("PulseSensor object created");
  }

  BPM = pulseSensor.getBeatsPerMinute();              

}


/* 
  Measures Heart Rate.
  Params : N/A
  Outputs: N/A
*/
void bed_HR_detect() 
{  
	Signal = analogRead(BED_HEART_PIN);   /* Read the sensor value */

	Serial.println(Signal);               /* Send the signal value */
}
