// whole.c
#include <stdio.h>
#include <stdlib.h>

static long int filesize(FILE* fp) {
  fseek(fp, 0, SEEK_END);
  long int size = ftell(fp);
  fseek(fp, 0, SEEK_SET);
  return size;
}

static int countline(char* block) {
  int line = 0;

  for(int i=0, flag=0; block[i]; i++)
    switch(block[i]) {
    case '\r': line++; flag=1; break;
    case '\n': if(flag) flag = 0; else line++; break;
    default: flag = 0;
    }

  return line+2;
}

static char* nextline(char* str) {
  char* n;
  for(n=str; *n!='\n' && *n!='\r' && *n!='\0'; n++);
  switch(*n) {
  case '\0': return NULL;
  case '\r': *n++='\0'; if(*n=='\n') n++; if(*n=='\0') return NULL; break;
  case '\n': *n++='\0'; if(*n=='\0') return NULL; break;
  }
  return n;
}

static char* readall(const char* const filename) {
  FILE* fp = fopen(filename, "rb");
  if(fp==NULL) {perror(NULL); exit(EXIT_FAILURE); }
  int size = filesize(fp);
  char* block = malloc(size+1);
  if(block==NULL) {perror(NULL); exit(EXIT_FAILURE); }
  int read_size = fread(block, 1, size, fp);
  fclose(fp);
  block[read_size]='\0';
  return block;
}

static char** split(char* block) {
  int linelength=countline(block);
  char** lines = malloc(linelength*sizeof(char*));
  if(lines==NULL) {perror(NULL); exit(EXIT_FAILURE); }
  char** p;
  for(p=lines; block!=NULL; block=nextline(block)) *p++=block;
  *p=NULL;
  return lines;
}

char** whole(const char* const filename) {
  char* block = readall(filename);
  return split(block);
}

void freewhole(char** m) {
  free(m[0]);
  free(m);
}