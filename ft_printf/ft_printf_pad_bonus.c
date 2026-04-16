/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_pad_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_bonus.h"

int	left_pad(t_fmt *f, int pad_width)
{
	if (f->minus)
		return (0);
	if (ft_pad(' ', pad_width) < 0)
		return (-1);
	return (pad_width);
}

int	right_pad(t_fmt *f, int pad_width)
{
	if (!f->minus)
		return (0);
	if (ft_pad(' ', pad_width) < 0)
		return (-1);
	return (pad_width);
}

int	left_pad_c(t_fmt *f, int pad_width, char c)
{
	if (f->minus)
		return (0);
	if (ft_pad(c, pad_width) < 0)
		return (-1);
	return (pad_width);
}

int	finalize(t_fmt *f, int emit_r, int w3, int total)
{
	int	rp;

	if (emit_r < 0)
		return (-1);
	rp = right_pad(f, w3);
	if (rp < 0)
		return (-1);
	return (total + emit_r + rp);
}
