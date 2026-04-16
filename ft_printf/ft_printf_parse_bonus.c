/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_parse_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_bonus.h"

static void	init_fmt(t_fmt *f)
{
	f->minus = 0;
	f->zero = 0;
	f->hash = 0;
	f->plus = 0;
	f->space = 0;
	f->width = 0;
	f->prec = 0;
	f->has_prec = 0;
	f->spec = 0;
}

static int	set_flag(char c, t_fmt *f)
{
	if (c == '-')
		f->minus = 1;
	else if (c == '0')
		f->zero = 1;
	else if (c == '#')
		f->hash = 1;
	else if (c == '+')
		f->plus = 1;
	else if (c == ' ')
		f->space = 1;
	else
		return (0);
	return (1);
}

static void	parse_digits(const char *fmt, size_t *i, int *val)
{
	*val = 0;
	while (fmt[*i] >= '0' && fmt[*i] <= '9')
	{
		*val = *val * 10 + (fmt[*i] - '0');
		*i += 1;
	}
}

static void	parse_precision(const char *fmt, size_t *i, t_fmt *f)
{
	f->has_prec = 1;
	*i += 1;
	parse_digits(fmt, i, &f->prec);
}

int	parse_format(const char *fmt, size_t *i, t_fmt *f)
{
	init_fmt(f);
	*i += 1;
	while (fmt[*i])
	{
		if (set_flag(fmt[*i], f) && (fmt[*i] != '0' || f->width == 0))
			*i += 1;
		else if (fmt[*i] >= '0' && fmt[*i] <= '9')
			parse_digits(fmt, i, &f->width);
		else if (fmt[*i] == '.')
			parse_precision(fmt, i, f);
		else
			break ;
	}
	if (!fmt[*i])
		return (-1);
	f->spec = fmt[*i];
	*i += 1;
	return (0);
}
