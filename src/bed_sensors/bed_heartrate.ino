#include <stdio.h>
#include "bed_errors.h"

#define samp_siz 20
#define rise_threshold 4

int sensorPin = 0;
float reads[samp_siz], sum;
    long int now, ptr;
    float mov_avg, reader, start;
    float first, second, third, before, print_value;
    bool rising;
    int rise_count;
    int n;
    long int last_beat;

/*  
    Author: Jonathan Hai
    Date: 2022-11-16
    Definition: Initializes heart rate sensor.
*/
int32_t bed_init_HR(){
    

    int32_t HR_init_error_code = BED_ERR_NONE;

    for (int i = 0; i < samp_siz; i++)
      reads[i] = 0;
    sum = 0;
    ptr = 0;

    //Error code currently is being pressured by powerful entities to say all is well.
    if(false){
        HR_init_error_code = BED_ERR_HEART_RATE;
    }
    return HR_init_error_code;
}

/*  
    Author: Jonathan Hai
    Date: 2022-11-16
    Definition: Reads analog pin for input from heart rate sensor, plots onto Arduino serial plotter.
*/

int32_t bed_HR_loop(){

    int32_t HR_loop_error_code = BED_ERR_NONE;
      // calculate an average of the sensor
      // during a 20 ms period (this will eliminate
      // the 50 Hz noise caused by electric light
      int32_t n = 0;
      float start = millis();
      float reader = 0;
      do
      {
        reader += analogRead (sensorPin);
        n++;
        now = millis();
      }
      while (now < start + 20);  
      reader /= n;  // we got an average
      
      // Add the newest measurement to an array
      // and subtract the oldest measurement from the array
      // to maintain a sum of last measurements
      sum -= reads[ptr];
      sum += reader;
      reads[ptr] = reader;
      mov_avg = sum / samp_siz;
      // now mov_avg holds the average of the values in the array

      // check for a rising curve (= a heart beat)
      if (mov_avg > before)
      {
        rise_count++;
        if (!rising && rise_count > rise_threshold)
        {
          // Ok, we have detected a rising curve, which implies a heartbeat.
          // Record the time since last beat, keep track of the two previous
          // times (first, second, third) to get a weighed average.
          // The rising flag prevents us from detecting the same rise more than once.
          rising = true;
          first = millis() - last_beat;
          last_beat = millis();

          // Calculate the weighed average of heartbeat rate
          // according to the three last beats
          print_value = 60000. / (0.4 * first + 0.3 * second + 0.3 * third);
          Serial.print("Heart rate (BPM): ");
          Serial.print(print_value);
          Serial.print('\n');
          
          third = second;
          second = first;
          
        }
      }
      else
      {
        // Ok, the curve is falling
        rising = false;
        rise_count = 0;
      }
      before = mov_avg;
      
      
      ptr++;
      ptr %= samp_siz;

    if(false){
        HR_loop_error_code = BED_ERR_HEART_RATE;
    }
    return HR_loop_error_code;
}