/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 00:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 00:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

static char	*append_buf_b(char *stash, char *buf)
{
	char	*old;

	old = stash;
	stash = ft_strjoin_b(stash, buf);
	if (old)
		free(old);
	return (stash);
}

static char	*read_stash(int fd, char *stash)
{
	char	*buf;
	int		bytes;

	buf = (char *)malloc(BUFFER_SIZE + 1);
	if (!buf)
		return (NULL);
	bytes = 1;
	while (!ft_strchr_b(stash, '\n') && bytes > 0)
	{
		bytes = read(fd, buf, BUFFER_SIZE);
		if (bytes == -1)
			break ;
		buf[bytes] = '\0';
		stash = append_buf_b(stash, buf);
		if (!stash)
			break ;
	}
	free(buf);
	if (bytes == -1 && stash)
		free(stash);
	if (bytes == -1)
		return (NULL);
	return (stash);
}

char	*get_next_line(int fd)
{
	static char	*stash[MAX_FD];
	char		*line;

	if (fd < 0 || fd >= MAX_FD || BUFFER_SIZE <= 0)
		return (NULL);
	stash[fd] = read_stash(fd, stash[fd]);
	if (!stash[fd])
		return (NULL);
	if (!stash[fd][0])
	{
		free(stash[fd]);
		stash[fd] = NULL;
		return (NULL);
	}
	line = ft_extract_line_b(stash[fd]);
	stash[fd] = ft_update_stash_b(stash[fd]);
	return (line);
}
