#include "ft_printf.h"

static int	print_format(char c, va_list *ap)
{
	if (c == 'c')
		return (ft_putchar((char)va_arg(*ap, int)));
	if (c == 's')
		return (ft_putstr(va_arg(*ap, char *)));
	if (c == 'p')
		return (ft_putptr((unsigned long)va_arg(*ap, void *)));
	if (c == 'd' || c == 'i')
		return (ft_putnbr(va_arg(*ap, int)));
	if (c == 'u')
		return (ft_putunbr(va_arg(*ap, unsigned int)));
	if (c == 'x')
		return (ft_puthex(va_arg(*ap, unsigned int), 0));
	if (c == 'X')
		return (ft_puthex(va_arg(*ap, unsigned int), 1));
	if (c == '%')
		return (ft_putchar('%'));
	if (ft_putchar('%') < 0 || ft_putchar(c) < 0)
		return (-1);
	return (2);
}

int	ft_printf(const char *format, ...)
{
	va_list	ap;
	int		count;
	int		ret;
	int		i;

	va_start(ap, format);
	count = 0;
	i = 0;
	while (format[i])
	{
		if (format[i] == '%' && format[i + 1])
			ret = print_format(format[++i], &ap);
		else
			ret = ft_putchar(format[i]);
		if (ret < 0)
			return (va_end(ap), -1);
		count += ret;
		i++;
	}
	va_end(ap);
	return (count);
}
