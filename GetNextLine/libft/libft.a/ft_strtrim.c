/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/04 11:27:52 by hiden             #+#    #+#             */
/*   Updated: 2026/03/04 12:51:31 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*array;
	int		start;
	int		end;
	int		i;

	start = 0;
	end = (int)ft_strlen(s1) - 1;
	while (s1[start] && ft_strchr(set, s1[start]))
		start++;
	while (end > start && ft_strchr(set, s1[end]))
		end--;
	array = (char *)malloc(sizeof(char) * (end - start + 2));
	if (!array)
		return (NULL);
	i = 0;
	while (start <= end)
		array[i++] = s1[start++];
	array[i] = '\0';
	return (array);
}
