/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 17:19:17 by hiden             #+#    #+#             */
/*   Updated: 2026/03/04 09:54:31 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*array;
	int		i;

	i = 0;
	array = (char *)malloc((ft_strlen(s) + 1) * sizeof(char));
	if (!array)
		return (NULL);
	while (s[i])
	{
		array[i] = s[i];
		i++;
	}
	array[i] = '\0';
	return (array);
}
