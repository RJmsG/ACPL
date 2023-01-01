#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

// same as linking files, but i dont need to link it :)
#include "whole.h"
#include "whole.c"

char** str_split(char* a_str, const char a_delim) {
    char** result    = 0;
    size_t count     = 0;
    char* tmp        = a_str;
    char* last_comma = 0;
    char delim[2];
    delim[0] = a_delim;
    delim[1] = 0;

    /* Count how many elements will be extracted. */
    while (*tmp)
    {
        if (a_delim == *tmp)
        {
            count++;
            last_comma = tmp;
        }
        tmp++;
    }

    /* Add space for trailing token. */
    count += last_comma < (a_str + strlen(a_str) - 1);

    /* Add space for terminating null string so caller
       knows where the list of returned strings ends. */
    count++;

    result = malloc(sizeof(char*) * count);

    if (result)
    {
        size_t idx  = 0;
        char* token = strtok(a_str, delim);

        while (token)
        {
            assert(idx < count);
            *(result + idx++) = strdup(token);
            token = strtok(0, delim);
        }
        assert(idx == count - 1);
        *(result + idx) = 0;
    }

    return result;
}

void compln(char **args) {
  printf( "nothing yet lol");
}

//  THIS IS THE MAIN FUNC! (axe has bad eyesight, so he needs a reminder of where everything is :skull:)
void main(){  
char** tokens;

char** lines = whole("Test.txt");
for(int i=0; lines[i]; i++) printf("%d %s\n", i, lines[i]);
int i;

char *str = strdup(lines[0]);
printf("months=[%s]\n\n", str);
tokens = str_split(str, ' ');
if (tokens)
{
for (i = 0; *(tokens + i); i++)
{
printf("month=[%s]\n", *(tokens + i));
free(*(tokens + i));
}
printf("\n");
compln(tokens);
free(tokens);
}
freewhole(lines);
//  end of main function
}