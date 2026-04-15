/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 21:20:59 by hiden             #+#    #+#             */
/*   Updated: 2026/03/04 10:50:25 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	number_len(int n)
{
	int	len;

	len = 0;
	if (n <= 0)
		len = 1;
	while (n != 0)
	{
		n = n / 10;
		len++;
	}
	return (len);
}

static long int	ft_check(int n, char *array)
{
	long int	nb;

	nb = n;
	if (nb == 0)
	{
		array[0] = '0';
		return (0);
	}
	if (nb < 0)
	{
		array[0] = '-';
		nb = -nb;
	}
	return (nb);
}

char	*ft_itoa(int n)
{
	int			len;
	char		*array;
	long int	nb;

	len = number_len(n);
	array = (char *)malloc(sizeof(char) * (len + 1));
	if (!array)
		return (NULL);
	array[len] = '\0';
	nb = ft_check(n, array);
	while (nb != 0)
	{
		len--;
		array[len] = (nb % 10) + '0';
		nb = nb / 10;
	}
	return (array);
}
