/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_int_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_bonus.h"
#include "ft_printf_num_bonus.h"

static void	int_sign(int n, t_fmt *f, unsigned long *v, char *sign)
{
	*sign = 0;
	if (n < 0)
	{
		*sign = '-';
		*v = (unsigned long)(-(long)n);
		return ;
	}
	*v = (unsigned long)n;
	if (f->plus)
		*sign = '+';
	else if (f->space)
		*sign = ' ';
}

static int	emit_int(char sign, unsigned long v, int zeros, int digits)
{
	int	total;

	total = 0;
	if (sign && ft_putch(sign) < 0)
		return (-1);
	if (sign)
		total += 1;
	if (ft_pad('0', zeros) < 0)
		return (-1);
	total += zeros;
	if (digits == 0 && v == 0)
		return (total);
	if (write_ulong(v) < 0)
		return (-1);
	return (total + digits);
}

static void	compute_widths(t_fmt *f, unsigned long v, char sign, int *w)
{
	w[0] = ulong_len(v);
	if (f->has_prec && f->prec == 0 && v == 0)
		w[0] = 0;
	w[1] = 0;
	if (f->has_prec && f->prec > w[0])
		w[1] = f->prec - w[0];
	w[2] = w[0] + w[1] + (sign != 0);
	w[3] = 0;
	if (f->width > w[2])
		w[3] = f->width - w[2];
}

int	print_int(t_fmt *f, va_list *ap)
{
	unsigned long	v;
	char			sign;
	int				w[4];
	int				total;
	int				r;

	int_sign(va_arg(*ap, int), f, &v, &sign);
	compute_widths(f, v, sign, w);
	total = 0;
	if (!f->minus && (!f->zero || f->has_prec))
	{
		r = left_pad(f, w[3]);
		if (r < 0)
			return (-1);
		total += r;
	}
	if (!f->minus && f->zero && !f->has_prec)
		w[1] += w[3];
	return (finalize(f, emit_int(sign, v, w[1], w[0]), w[3], total));
}
