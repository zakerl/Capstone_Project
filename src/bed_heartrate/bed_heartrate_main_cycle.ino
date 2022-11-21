#include <stdio.h>
#include "bed_errors.h"

// int sensorPin = 0;

void setup() {
    Serial.begin(9600);
    uint32_t HR_error_code;
    HR_error_code = bed_init_HR();
    if(HR_error_code != BED_ERR_NONE)
    {
        Serial.print("Program Failed due to heart rate init error:\t");
        Serial.println((int16_t)HR_error_code);
    }
    HR_error_code = bed_HR_serial_plot();
    if(HR_error_code != BED_ERR_NONE)
    {
        Serial.print("Program Failed due to heart rate loop error:\t");
        Serial.println((int16_t)HR_error_code);
    }
}

void loop (){
    
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
          // Serial.print("Heart rate (BPM): ");
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

    
}