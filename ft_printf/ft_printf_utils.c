/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hakuta <hakuta@student.42tokyo.jp>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/28 17:54:41 by hakuta            #+#    #+#             */
/*   Updated: 2026/04/29 18:28:06 by hakuta           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putchar(char c)
{
	ssize_t	ret;

	ret = write(1, &c, 1);
	if (ret < 0)
		return (-1);
	return (1);
}




int	ft_putstr(char *s)
{
	size_t	count;
	ssize_t	ret;

	if (!s)
		return (ft_putstr("(null)"));
	count = 0;
	while (s[count])
		count++;
	if (count == 0)
		return (0);
	ret = write(1, s, count);
	if (ret == -1)
		return (-1);
	return ((int)ret);
}
