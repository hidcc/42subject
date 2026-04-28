/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hakuta <hakuta@student.42tokyo.jp>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/22 21:16:24 by hakuta            #+#    #+#             */
/*   Updated: 2026/04/23 18:55:58 by hakuta           ###   ########.fr       */
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

static long int	prepare_number(int n, char *array)
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
	array = malloc(len + 1);
	if (!array)
		return (NULL);
	array[len] = '\0';
	nb = prepare_number(n, array);
	while (nb != 0)
	{
		len--;
		array[len] = (nb % 10) + '0';
		nb = nb / 10;
	}
	return (array);
}
