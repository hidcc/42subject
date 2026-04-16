/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_bonus.h"

int	ft_putch(char c)
{
	if (write(1, &c, 1) < 0)
		return (-1);
	return (1);
}

int	ft_write_str(const char *s, int len)
{
	int	w;

	if (len <= 0)
		return (0);
	w = (int)write(1, s, (size_t)len);
	if (w < 0)
		return (-1);
	return (w);
}

int	ft_strlen_b(const char *s)
{
	int	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

int	ft_pad(char c, int n)
{
	int	i;

	i = 0;
	while (i < n)
	{
		if (ft_putch(c) < 0)
			return (-1);
		i++;
	}
	return (n);
}
