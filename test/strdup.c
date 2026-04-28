




#include <string.h>

char *(const char *s1)
{
    int i;
    char *ptr;

    i = 0;
    ptr = malloc(strlen(s1) + 1)
    while(s1[i])
    {
        ptr[i] = s1[i];
        i++;
    }
    ptr[i] = '\0';
    return ptr;
}