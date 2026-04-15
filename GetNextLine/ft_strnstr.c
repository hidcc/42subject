/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 16:15:44 by hiden             #+#    #+#             */
/*   Updated: 2026/03/03 19:58:12 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *s1, const char *s2, size_t len)
{
	size_t	i;
	size_t	j;

	if (s2[0] == '\0')
		return ((char *)s1);
	i = 0;
	while (s1[i] && i < len)
	{
		j = 0;
		while (s2[j] && s1[i + j] == s2[j] && i + j < len)
		{
			j++;
		}
		if (s2[j] == '\0')
			return ((char *)(&s1[i]));
		i++;
	}
	return (NULL);
}
