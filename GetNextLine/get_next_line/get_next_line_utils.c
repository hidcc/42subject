/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 13:52:36 by hiden             #+#    #+#             */
/*   Updated: 2026/03/06 14:16:01 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int	ft_strchr(char *str, char c)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] == c)
			return (1);
		i++;
	}
	return (0);
}

char	*ft_strjoin(char *str, char *buf)
{
	char	*join;
	size_t	str_len;
	size_t	buf_len;
	int		i;
	int		j;

	str_len = ft_strlen(str);
	buf_len = ft_strlen(buf);
	join = (char *)malloc(sizeof(char) * (str_len + buf_len + 1));
	i = 0;
	while (str[i])
	{
		join[i] = str[i];
		i++;
	}
	j = 0;
	while (buf[j])
	{
		join[i + j] = buf[j];
		j++;
	}
	join[j] = '\0';
	return (join);
}

size_t	ft_strlen(char *str)
{
	size_t	count;

	count = 0;
	while (str)
		count++;
	return (count);
}
