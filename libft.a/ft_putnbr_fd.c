/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hakuta <hakuta@student.42tokyo.jp>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/22 21:18:23 by hakuta            #+#    #+#             */
/*   Updated: 2026/04/23 14:03:47 by hakuta           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	long int	large_number;
	char		result;

	large_number = n;
	if (large_number < 0)
	{
		write(fd, "-", 1);
		large_number = -large_number;
	}
	if (large_number >= 10)
		ft_putnbr_fd(large_number / 10, fd);
	result = (large_number % 10) + '0';
	write(fd, &result, 1);
}
