/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hakuta <hakuta@student.42tokyo.jp>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/25 12:41:33 by hakuta            #+#    #+#             */
/*   Updated: 2026/04/25 12:41:36 by hakuta           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*read_until_newline(int fd, char *stash);
static int	read_chunk(int fd, char *buf, char **stash);

char	*get_next_line(int fd)
{
	static char	*stash;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	stash = read_until_newline(fd, stash);
	if (!stash || !*stash)
	{
		free(stash);
		stash = NULL;
		return (NULL);
	}
	line = ft_extract_line(stash);
	stash = ft_update_stash(stash);
	return (line);
}

static char	*read_until_newline(int fd, char *stash)
{
	char	*buf;

	if (stash && ft_strchr(stash, '\n'))
		return (stash);
	buf = malloc(BUFFER_SIZE + 1);
	if (!buf)
	{
		free(stash);
		return (NULL);
	}
	while (!ft_strchr(stash, '\n') && read_chunk(fd, buf, &stash))
		;
	free(buf);
	return (stash);
}

static int	read_chunk(int fd, char *buf, char **stash)
{
	ssize_t	n;

	n = read(fd, buf, BUFFER_SIZE);
	if (n < 0)
	{
		free(*stash);
		*stash = NULL;
		return (0);
	}
	if (n == 0)
		return (0);
	buf[n] = '\0';
	*stash = ft_strjoin_free(*stash, buf);
	return (*stash != NULL);
}
