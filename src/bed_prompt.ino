#include "WString.h"
#include "HardwareSerial.h"
#include "bed_prompt.h"

/*
    Author    : Anish Rangarajan
    Date      : 11/11/2022
    Defintion : Initializes the Prompt system.  
*/
void bed_init_prompt()
{ 
  int index = 0;
  Prompt prompts[PROMPT_NUMBER] =  {
                        { 1, 0, "Are you in pain ?",        "N/A"},
                        { 2, 0, "Where do you feel pain?",  "N/A"}
                       };
  Serial.println("Prompt Id:\t\t"       + (String)prompts[index].prompt_id);
  Serial.println("Prompt Triggered:\t"  + (String)prompts[index].prompt_triggered);
  Serial.println("Prompt Question:\t"   + (String)prompts[index].prompt_question);
  Serial.println("Prompt Answer:\t\t"   + (String)prompts[index].prompt_response);
}