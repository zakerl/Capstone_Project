/* Implementation file for touch bezel*/

#include "bed_touch.h"
#include "bed_hardware_pin_map.h"
#include "bed_display.h"

/*
    Author    : Anish Rangarajan
    Date      : 1/27/2023
    Defintion : Performs calculation and returns orientation(CW or CCW).
*/

int8_t bed_touch_detect(unsigned long currentTime)
{
    if (touchval[0] == 1 && touchval[1] == 1 && touchval[2] == 1 && touchval[3] == 1 && touchval[4] == 1)
    {
      if(touch.flag == 1 )
      {

        if(currentTime - prev_wait_time >= TOUCH_WAIT_TIME)
        {
          touch.flag                    = -1;
          touch.pad_is_touched_first    = -1;
          touch.pad_is_touched_second   = -1;     
          touch.releaseFlag             =  0;     
          prev_wait_time = currentTime;               
        }
        
        else
          touch.releaseFlag = 1; 
      }

      else 
      {
        touch.flag = -1;
        touch.releaseFlag = 0;
        touch.pad_is_touched_first = -1;
        touch.pad_is_touched_second = -1;     
        prev_wait_time = currentTime;
      }

    }

    if (touch.flag == -1) 
    {
      for (int i = 0; i < NO_OF_KEYS; i++) 
      {
        if (touchval[i] == 0) 
        {
          touch.flag = 1;
          touch.pad_is_touched_first = i;
          break;
        }
      }

      for(int i =0; i<NO_OF_KEYS; i++)
        firsttouch[i] = touchval[i];

    }

    if (touch.flag == 1)
    {

      if(touchval[touch.pad_is_touched_first] == 0 && touch.releaseFlag == 0)
        prev_wait_time = currentTime;

      if(touchval[touch.pad_is_touched_first] == 0 && touch.releaseFlag == 1) 
      {
        Serial.println(touch.pad_is_touched_first);

        switch (touch.pad_is_touched_first) 
        {
          case 0: 
                  touch.direction = 2;
                  break;

          case 1:
                  touch.direction = 5;
                  break;

          case 2:
                  touch.direction = 3;
                  break;

          case 4: 
                  touch.direction = 4;
                  break;          
      
          default:
                  touch.direction = 0;
        }

        
        touch.releaseFlag = 0;
        touch.flag = -1;
        touch.pad_is_touched_first = -1;
        touch.pad_is_touched_second = -1;
        prev_wait_time = currentTime;
        return touch.direction;
      }
      
      for (int i = 0; i < NO_OF_KEYS; i++) 
      {
        if (touchval[i] != firsttouch[i] && touchval[i] == 0) 
        {
          touch.flag = 2;
          touch.pad_is_touched_second = i;
          prev_wait_time = currentTime;
        }
      }
    }

    if (touch.flag == 2) 
    {
      
      if (touch.pad_is_touched_first == 0 && touch.pad_is_touched_second == NO_OF_KEYS-1) 
        touch.direction = 1;


      else if (touch.pad_is_touched_first == NO_OF_KEYS-1 && touch.pad_is_touched_second == 0)
        touch.direction = -1;       


      else if (touch.pad_is_touched_first > touch.pad_is_touched_second) 
        touch.direction = 1;

      else if (touch.pad_is_touched_first < touch.pad_is_touched_second) 
        touch.direction = -1;

      for(int i=0;i<NO_OF_KEYS;i++)
        firsttouch[i] = 1;

      touch.releaseFlag = 0;
      touch.flag = -1;
      touch.pad_is_touched_first = -1;
      touch.pad_is_touched_second = -1;
      prev_wait_time = currentTime;
      return touch.direction;
    }

  return 0;
}
