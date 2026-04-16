/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_bonus.h"

static int	dispatch(t_fmt *f, va_list *ap)
{
	if (f->spec == 'c')
		return (print_char(f, ap));
	if (f->spec == 's')
		return (print_str(f, ap));
	if (f->spec == '%')
		return (print_percent(f));
	if (f->spec == 'd' || f->spec == 'i')
		return (print_int(f, ap));
	if (f->spec == 'u')
		return (print_uint(f, ap));
	if (f->spec == 'x' || f->spec == 'X')
		return (print_hex(f, ap));
	if (f->spec == 'p')
		return (print_ptr(f, ap));
	return (ft_putch(f->spec));
}

static int	handle_spec(const char *fmt, size_t *i, va_list *ap, int *done)
{
	t_fmt	f;
	int		r;

	r = parse_format(fmt, i, &f);
	if (r < 0)
	{
		*done = 1;
		return (0);
	}
	return (dispatch(&f, ap));
}

int	ft_printf(const char *format, ...)
{
	va_list	ap;
	size_t	i;
	int		total;
	int		step;
	int		done;

	if (!format)
		return (-1);
	va_start(ap, format);
	total = 0;
	i = 0;
	done = 0;
	while (format[i] && !done)
	{
		if (format[i] == '%')
			step = handle_spec(format, &i, &ap, &done);
		else
			step = ft_putch(format[i++]);
		if (step < 0)
			return (va_end(ap), -1);
		total += step;
	}
	va_end(ap);
	return (total);
}
