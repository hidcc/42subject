/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_char_bonus.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_bonus.h"

static char	pad_char(t_fmt *f)
{
	if (f->zero && !f->minus)
		return ('0');
	return (' ');
}

int	print_char(t_fmt *f, va_list *ap)
{
	char	c;
	int		pad;
	int		r;
	int		total;

	c = (char)va_arg(*ap, int);
	pad = f->width - 1;
	if (pad < 0)
		pad = 0;
	r = left_pad_c(f, pad, pad_char(f));
	if (r < 0)
		return (-1);
	total = r + 1;
	if (ft_putch(c) < 0)
		return (-1);
	r = right_pad(f, pad);
	if (r < 0)
		return (-1);
	return (total + r);
}

int	print_percent(t_fmt *f)
{
	int	pad;
	int	r;
	int	total;

	pad = f->width - 1;
	if (pad < 0)
		pad = 0;
	r = left_pad_c(f, pad, pad_char(f));
	if (r < 0)
		return (-1);
	total = r + 1;
	if (ft_putch('%') < 0)
		return (-1);
	r = right_pad(f, pad);
	if (r < 0)
		return (-1);
	return (total + r);
}

static int	str_len(char *s, t_fmt *f)
{
	int	len;

	len = ft_strlen_b(s);
	if (f->has_prec && f->prec < len)
		len = f->prec;
	return (len);
}

int	print_str(t_fmt *f, va_list *ap)
{
	char	*s;
	int		len;
	int		pad;
	int		r;
	int		total;

	s = va_arg(*ap, char *);
	if (!s)
		s = "(null)";
	len = str_len(s, f);
	pad = f->width - len;
	if (pad < 0)
		pad = 0;
	r = left_pad_c(f, pad, pad_char(f));
	if (r < 0 || ft_write_str(s, len) < 0)
		return (-1);
	total = r + len;
	r = right_pad(f, pad);
	if (r < 0)
		return (-1);
	return (total + r);
}
