/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include "ft_printf_internal.h"

static int	dispatch(char spec, va_list *ap)
{
	if (spec == 'c')
		return (ft_putchar((char)va_arg(*ap, int)));
	if (spec == 's')
		return (ft_putstr(va_arg(*ap, char *)));
	if (spec == 'p')
		return (ft_putptr(va_arg(*ap, void *)));
	if (spec == 'd' || spec == 'i')
		return (ft_putnbr(va_arg(*ap, int)));
	if (spec == 'u')
		return (ft_putunbr(va_arg(*ap, unsigned int)));
	if (spec == 'x')
		return (ft_puthex(va_arg(*ap, unsigned int), 0));
	if (spec == 'X')
		return (ft_puthex(va_arg(*ap, unsigned int), 1));
	if (spec == '%')
		return (ft_putchar('%'));
	return (-1);
}

static int	handle_spec(const char *fmt, size_t *i, va_list *ap)
{
	int	ret;

	*i += 1;
	if (fmt[*i] == '\0')
		return (-1);
	ret = dispatch(fmt[*i], ap);
	if (ret >= 0)
		*i += 1;
	return (ret);
}

int	ft_printf(const char *format, ...)
{
	va_list	ap;
	size_t	i;
	int		total;
	int		step;

	if (!format)
		return (-1);
	va_start(ap, format);
	total = 0;
	i = 0;
	while (format[i])
	{
		if (format[i] == '%')
			step = handle_spec(format, &i, &ap);
		else
		{
			step = ft_putchar(format[i]);
			i++;
		}
		if (step < 0)
			return (va_end(ap), -1);
		total += step;
	}
	va_end(ap);
	return (total);
}
