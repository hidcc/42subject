/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 00:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/25 00:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

static char	*read_until_newline(int fd, char *stash);
static int	read_chunk(int fd, char *buf, char **stash);

char	*get_next_line(int fd)
{
	static char	*stash[MAX_FD];
	char		*line;

	if (fd < 0 || fd >= MAX_FD || BUFFER_SIZE <= 0)
		return (NULL);
	stash[fd] = read_until_newline(fd, stash[fd]);
	if (!stash[fd])
		return (NULL);
	if (!*stash[fd])
	{
		free(stash[fd]);
		stash[fd] = NULL;
		return (NULL);
	}
	line = ft_extract_line(stash[fd]);
	stash[fd] = ft_update_stash(stash[fd]);
	return (line);
}

static char	*read_until_newline(int fd, char *stash)
{
	char	*buf;
	int		more;

	buf = malloc(BUFFER_SIZE + 1);
	if (!buf)
	{
		free(stash);
		return (NULL);
	}
	more = 1;
	while (more == 1 && !ft_strchr(stash, '\n'))
		more = read_chunk(fd, buf, &stash);
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
	if (!*stash)
		return (0);
	return (1);
}
