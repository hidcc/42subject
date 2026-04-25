/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils_bonus.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hakuta <hakuta@student.42tokyo.jp>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/25 12:41:18 by hakuta            #+#    #+#             */
/*   Updated: 2026/04/25 12:41:20 by hakuta           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

size_t	ft_strlen(const char *s)
{
	size_t	i;

	if (!s)
		return (0);
	i = 0;
	while (s[i])
		i++;
	return (i);
}

char	*ft_strchr(const char *s, int c)
{
	if (!s)
		return (NULL);
	while (*s)
	{
		if (*s == (char)c)
			return ((char *)s);
		s++;
	}
	if ((char)c == '\0')
		return ((char *)s);
	return (NULL);
}

char	*ft_strjoin_free(char *s1, const char *s2)
{
	size_t	a;
	size_t	b;
	size_t	i;
	char	*out;

	a = ft_strlen(s1);
	b = ft_strlen(s2);
	out = malloc(a + b + 1);
	if (!out)
	{
		free(s1);
		return (NULL);
	}
	i = 0;
	while (i < a + b)
	{
		if (i < a)
			out[i] = s1[i];
		else
			out[i] = s2[i - a];
		i++;
	}
	out[a + b] = '\0';
	free(s1);
	return (out);
}

char	*ft_extract_line(const char *stash)
{
	char	*line;
	size_t	i;

	if (!stash || !*stash)
		return (NULL);
	i = 0;
	while (stash[i] && stash[i] != '\n')
		i++;
	if (stash[i] == '\n')
		i++;
	line = malloc(i + 1);
	if (!line)
		return (NULL);
	i = 0;
	while (stash[i] && stash[i] != '\n')
	{
		line[i] = stash[i];
		i++;
	}
	if (stash[i] == '\n')
		line[i++] = '\n';
	line[i] = '\0';
	return (line);
}

char	*ft_update_stash(char *stash)
{
	char	*rest;
	size_t	i;
	size_t	j;

	i = 0;
	while (stash[i] && stash[i] != '\n')
		i++;
	if (!stash[i] || !stash[i + 1])
	{
		free(stash);
		return (NULL);
	}
	rest = malloc(ft_strlen(stash) - i);
	if (!rest)
	{
		free(stash);
		return (NULL);
	}
	j = 0;
	i++;
	while (stash[i])
		rest[j++] = stash[i++];
	rest[j] = '\0';
	free(stash);
	return (rest);
}
