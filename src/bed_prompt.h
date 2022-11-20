/* Header file for the Prompt System */
#ifndef BED_PROMPT_H
#define BED_PROMPT_H

/* Includes*/
#include <stdint.h>
#include <stdio.h>

/* Definitions*/
#define PROMPT_NUMBER     3

/* Structure Definitions */
typedef struct PROMPT_Tag
{
  uint16_t    prompt_id;                /* Represents the type of prompt                          */  
  uint16_t    prompt_triggered;         /* Represents whether or not prompt was triggered         */
  char*       prompt_question;          /* Represents the question asked to the user              */
  char*       prompt_possible_answers;  /* Represnts the possible answers to the prompt question  */
  char*       prompt_response;          /* Represents the users response                          */
}Prompt;

/*Global Declaration*/
Prompt prompts[PROMPT_NUMBER] = 
                        {
                          { 1, 0, "Is the device on ?"          , "Yes-No"          , "N/A"},                          
                          { 2, 0, "Are you in pain ?"           , "Yes-No"          , "N/A"},
                          { 3, 0, "Are you Seated or Standing ?", "Seated-Standing" , "N/A"}
                        }; 


#endif