/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_internal.h"

static int	put_ulong(unsigned long n)
{
	int	len;
	int	r;

	if (n >= 10)
	{
		len = put_ulong(n / 10);
		if (len < 0)
			return (-1);
		r = ft_putchar((char)('0' + (n % 10)));
		if (r < 0)
			return (-1);
		return (len + r);
	}
	return (ft_putchar((char)('0' + n)));
}

int	ft_putnbr(int n)
{
	unsigned long	v;
	int				sign;
	int				r;

	sign = 0;
	if (n < 0)
	{
		sign = ft_putchar('-');
		if (sign < 0)
			return (-1);
		v = (unsigned long)(-(long)n);
	}
	else
		v = (unsigned long)n;
	r = put_ulong(v);
	if (r < 0)
		return (-1);
	return (sign + r);
}

int	ft_putunbr(unsigned int n)
{
	return (put_ulong((unsigned long)n));
}
