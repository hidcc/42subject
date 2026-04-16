/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_bonus.h                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hiden <hiden@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/16 10:00:00 by hiden             #+#    #+#             */
/*   Updated: 2026/04/16 10:00:00 by hiden            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_BONUS_H
# define FT_PRINTF_BONUS_H

# include <stdarg.h>
# include <stddef.h>
# include <unistd.h>

typedef struct s_fmt
{
	int		minus;
	int		zero;
	int		hash;
	int		plus;
	int		space;
	int		width;
	int		prec;
	int		has_prec;
	char	spec;
}	t_fmt;

int		ft_printf(const char *format, ...);

int		ft_putch(char c);
int		ft_write_str(const char *s, int len);
int		ft_strlen_b(const char *s);
int		ft_pad(char c, int n);

int		parse_format(const char *fmt, size_t *i, t_fmt *f);

int		left_pad(t_fmt *f, int pad_width);
int		right_pad(t_fmt *f, int pad_width);
int		left_pad_c(t_fmt *f, int pad_width, char c);
int		finalize(t_fmt *f, int emit_r, int w3, int total);

int		print_char(t_fmt *f, va_list *ap);
int		print_str(t_fmt *f, va_list *ap);
int		print_percent(t_fmt *f);
int		print_int(t_fmt *f, va_list *ap);
int		print_uint(t_fmt *f, va_list *ap);
int		print_hex(t_fmt *f, va_list *ap);
int		print_ptr(t_fmt *f, va_list *ap);

#endif
