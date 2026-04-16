/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_num_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_bonus.h"
#include "ft_printf_num_bonus.h"

int	ulong_len(unsigned long n)
{
	int	len;

	len = 0;
	if (n == 0)
		return (1);
	while (n > 0)
	{
		n /= 10;
		len++;
	}
	return (len);
}

int	write_ulong(unsigned long n)
{
	char	buf[32];
	int		i;

	i = 0;
	if (n == 0)
		buf[i++] = '0';
	while (n > 0)
	{
		buf[i++] = (char)('0' + (n % 10));
		n /= 10;
	}
	while (--i >= 0)
	{
		if (ft_putch(buf[i]) < 0)
			return (-1);
	}
	return (0);
}

int	hex_len(unsigned long n)
{
	int	len;

	len = 0;
	if (n == 0)
		return (1);
	while (n > 0)
	{
		n /= 16;
		len++;
	}
	return (len);
}

int	write_hex(unsigned long n, const char *digits)
{
	char	buf[32];
	int		i;

	i = 0;
	if (n == 0)
		buf[i++] = '0';
	while (n > 0)
	{
		buf[i++] = digits[n % 16];
		n /= 16;
	}
	while (--i >= 0)
	{
		if (ft_putch(buf[i]) < 0)
			return (-1);
	}
	return (0);
}
