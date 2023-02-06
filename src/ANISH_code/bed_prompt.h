/* Header file for the Prompt System */
#ifndef BED_PROMPT_H
#define BED_PROMPT_H

/* Includes*/
#include <stdint.h>
#include <stdio.h>

/* Definitions*/

#define MAX_PROMPTS 7
/* Structure Definitions */
typedef struct PROMPT_Tag
{
  uint16_t    prompt_id;                /* Represents the type of prompt                          */  
  uint16_t    no_of_options;         /* Represents whether or not prompt was triggered         */
  char*       prompt_question;          /* Represents the question asked to the user              */
  char        prompt_possible_answers[80];  /* Represnts the possible answers to the prompt question  */
  char*       prompt_response;          /* Represents the users response                          */
}Prompt;

/*Global Declaration*/
Prompt test[1] = 
{
  { 1, 2, "Is the device on ?"          , "Yes-No"                      , "N/A"},                          
}; 

Prompt prompt_walking[3] = 
{                          
  { 1, 3, "Why did u stop"              , "Pain-Break-Other"            , "N/A"},
  { 2, 5, "Where do u feel pain ?"      , "Arms-Legs-Back-Torso-Other"  , "N/A"},
  { 3, 7, "Pain Level ?"                , "1-2-3-4-5-6-7"               , "N/A"}
}; 


#endif