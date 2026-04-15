/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 20:53:06 by hiden             #+#    #+#             */
/*   Updated: 2026/03/03 21:17:38 by hiden            ###   ########.fr       */
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
