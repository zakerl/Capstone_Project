/* Header file for the Prompt System */

#include <stdio.h>

#define PROMPT_NUMBER     2
typedef struct PROMPT_Tag
{
  uint16_t    prompt_id;        /* Represents the type of prompt*/  
  uint16_t    prompt_triggered; /* Represents whether or not prompt was triggered*/
  char*       prompt_question;  /* Represents the question asked to the user*/
  char*       prompt_response;  /* Represents the users response*/
}Prompt;

void bed_init_prompt();