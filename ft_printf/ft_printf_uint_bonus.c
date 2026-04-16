/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_uint_bonus.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_bonus.h"
#include "ft_printf_num_bonus.h"

static int	emit_uint(unsigned long v, int zeros, int digits)
{
	int	total;

	total = 0;
	if (ft_pad('0', zeros) < 0)
		return (-1);
	total += zeros;
	if (digits == 0 && v == 0)
		return (total);
	if (write_ulong(v) < 0)
		return (-1);
	return (total + digits);
}

static void	compute_widths(t_fmt *f, unsigned long v, int *w)
{
	w[0] = ulong_len(v);
	if (f->has_prec && f->prec == 0 && v == 0)
		w[0] = 0;
	w[1] = 0;
	if (f->has_prec && f->prec > w[0])
		w[1] = f->prec - w[0];
	w[2] = w[0] + w[1];
	w[3] = 0;
	if (f->width > w[2])
		w[3] = f->width - w[2];
}

int	print_uint(t_fmt *f, va_list *ap)
{
	unsigned long	v;
	int				w[4];
	int				total;
	int				r;

	v = (unsigned long)va_arg(*ap, unsigned int);
	compute_widths(f, v, w);
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
	return (finalize(f, emit_uint(v, w[1], w[0]), w[3], total));
}
