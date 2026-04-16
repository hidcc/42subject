/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_internal.h"

static int	put_ulong_hex(unsigned long n, const char *digits)
{
	int	len;
	int	r;

	if (n >= 16)
	{
		len = put_ulong_hex(n / 16, digits);
		if (len < 0)
			return (-1);
		r = ft_putchar(digits[n % 16]);
		if (r < 0)
			return (-1);
		return (len + r);
	}
	return (ft_putchar(digits[n]));
}

int	ft_puthex(unsigned int n, int upper)
{
	const char	*digits;

	if (upper)
		digits = "0123456789ABCDEF";
	else
		digits = "0123456789abcdef";
	return (put_ulong_hex((unsigned long)n, digits));
}

int	ft_putptr(void *p)
{
	unsigned long	addr;
	int				r;
	int				total;

	addr = (unsigned long)p;
	r = ft_putstr("0x");
	if (r < 0)
		return (-1);
	total = put_ulong_hex(addr, "0123456789abcdef");
	if (total < 0)
		return (-1);
	return (r + total);
}
