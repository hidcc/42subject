#include "ft_printf.h"

int	ft_putchar(char c)
{
	if (write(1, &c, 1) < 0)
		return (-1);
	return (1);
}

int	ft_putstr(char *s)
{
	int	count;

	if (!s)
		return (ft_putstr("(null)"));
	count = 0;
	while (s[count])
		count++;
	if (count > 0 && write(1, s, count) < 0)
		return (-1);
	return (count);
}
