#include "ft_printf.h"
#include <stdio.h>

int main(void)
{
    ft_printf("c=%c s=%s p=%p d=%d i=%i u=%u x=%x X=%X %%\n",
              'A', "hello", (void *)1000, -42, 42, 4294967295u, 255, 255);
    printf("c=%c s=%s p=%p d=%d i=%i u=%u x=%x X=%X %%\n",
              'A', "hello", (void *)1000, -42, 42, 4294967295u, 255, 255);   
    return (0);
}