/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_nbr.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hakuta <hakuta@student.42tokyo.jp>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/28 17:54:47 by hakuta            #+#    #+#             */
/*   Updated: 2026/04/29 10:13:40 by hakuta           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putunbr_base(unsigned long n, char *base)
{
	int	len;
	int	ret;
	int	r;

	len = 0;
	while (base[len])
		len++;
	ret = 0;
	if (n >= (unsigned long)len)
	{
		ret = ft_putunbr_base(n / len, base);
		if (ret < 0)
			return (-1);
	}
	r = ft_putchar(base[n % len]);
	if (r < 0)
		return (-1);
	return (ret + 1);
}

int	ft_putnbr(int n)
{
	long	nb;
	int		ret;

	nb = n;
	if (nb < 0)
	{
		if (ft_putchar('-') < 0)
			return (-1);
		nb = -nb;
		ret = ft_putunbr_base((unsigned long)nb, "0123456789");
		if (ret < 0)
			return (-1);
		return (ret + 1);
	}
	return (ft_putunbr_base((unsigned long)nb, "0123456789"));
}

int	ft_putunbr(unsigned int n)
{
	return (ft_putunbr_base((unsigned long)n, "0123456789"));
}

int	ft_puthex(unsigned int n, int upper)
{
	if (upper)
		return (ft_putunbr_base((unsigned long)n, "0123456789ABCDEF"));
	return (ft_putunbr_base((unsigned long)n, "0123456789abcdef"));
}

int	ft_putptr(unsigned long ptr)
{
	int	ret;
	int	r2;

	ret = ft_putstr("0x");
	if (ret < 0)
		return (-1);
	r2 = ft_putunbr_base(ptr, "0123456789abcdef");
	if (r2 < 0)
		return (-1);
	return (ret + r2);
}
