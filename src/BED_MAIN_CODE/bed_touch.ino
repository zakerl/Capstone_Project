/* Implementation file for touch bezel*/

#include "bed_touch.h"
#include "bed_hardware_pin_map.h"
#include "bed_display.h"

/* 
  Checks the state of all touch pads and generates specific inputs.
  Params : currentTime: Current cycle of the program.
  Outputs: Type of input generated .
*/
int8_t bed_touch_detect(unsigned long currentTime)
{
  /* No pads are touched */
  if(touchval[0] && touchval[1] && touchval[2] && touchval[3] && touchval[4])
    {

      if(touch.flag == 1 )
      {       
        if(currentTime - prev_wait_time >= TOUCH_WAIT_TIME)
        {
          touch.flag = -1;
          touch.pad_is_touched_first = -1;
          touch.pad_is_touched_second = -1;
          touch.releaseFlag =  0;   
          prev_wait_time = currentTime;  
        }

        else 
        {
          touch.releaseFlag = 1; 
        }        
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

  /* Checking for touch input */
  if(touch.flag == -1)
  {
    for(int i = 0; i< NO_OF_KEYS; i++)
    {
      if(touchval[i] == 0)
      {
        touch.pad_is_touched_first = i;
        touch.flag = 1;
        break;
      }
    }

    for(int i =0; i<NO_OF_KEYS; i++)
    {
      firsttouch[i] = touchval[i];
    }
    
  }  

  /* First pad is touched */
  if(touch.flag == 1)
  {
    if(touchval[touch.pad_is_touched_first] == 0 && touch.releaseFlag == 0)
    {
      prev_wait_time = currentTime;
    }
        
     if(touchval[touch.pad_is_touched_first] == 0 && touch.releaseFlag == 1) 
      {

        switch (touch.pad_is_touched_first) 
        {
          case 0: 
                  touch.direction = 2;
                  break;

          case 1:
                  touch.direction = 3;
                  break;

          case 2:
                  touch.direction = 4;
                  break;

          case 3:
                  touch.direction = 5;
                  break;

          case 4: 
                  touch.direction = 6;
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
          prev_wait_time = currentTime;
          touch.flag = 2;
          touch.pad_is_touched_second = i;
          prev_wait_time = currentTime;
          break; 
        }
      }
      

  }

  /* Second pad is touched */
  if(touch.flag == 2)
  {
      if (touch.pad_is_touched_first == 0 && touch.pad_is_touched_second == NO_OF_KEYS-1) 
      {
        touch.direction = 1;
      }
        


      else if (touch.pad_is_touched_first == NO_OF_KEYS-1 && touch.pad_is_touched_second == 0)
        touch.direction = -1;       


      else if (touch.pad_is_touched_first > touch.pad_is_touched_second) 
        touch.direction = 1;

      else if (touch.pad_is_touched_first < touch.pad_is_touched_second) 
        touch.direction = -1;

      for(int i =0; i<NO_OF_KEYS; i++)
      {
        firsttouch[i] = touchval[i];
      }

      touch.releaseFlag = 0;
      touch.flag = -1;
      touch.pad_is_touched_first = -1;
      touch.pad_is_touched_second = -1;
      prev_wait_time = currentTime;
      return touch.direction;
  }

  return 0;
}

