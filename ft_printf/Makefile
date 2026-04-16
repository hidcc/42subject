# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hiden <hiden@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/16 10:00:00 by hiden              #+#    #+#             #
#    Updated: 2026/04/16 10:00:00 by hiden             ###   ########.fr       #
#                                                                              #
# **************************************************************************** #

NAME		= libftprintf.a

CC			= cc
CFLAGS		= -Wall -Wextra -Werror
AR			= ar rcs
RM			= rm -f

SRCS		= ft_printf.c \
			  ft_putchar.c \
			  ft_putnbr.c \
			  ft_puthex.c

BONUS_SRCS	= ft_printf_bonus.c \
			  ft_printf_utils_bonus.c \
			  ft_printf_parse_bonus.c \
			  ft_printf_pad_bonus.c \
			  ft_printf_num_bonus.c \
			  ft_printf_char_bonus.c \
			  ft_printf_int_bonus.c \
			  ft_printf_uint_bonus.c \
			  ft_printf_hex_bonus.c \
			  ft_printf_ptr_bonus.c

OBJS		= $(SRCS:.c=.o)
BONUS_OBJS	= $(BONUS_SRCS:.c=.o)

MAND_SENT	= .mandatory
BONUS_SENT	= .bonus

all: $(NAME)

$(NAME): $(MAND_SENT)

$(MAND_SENT):
	@if [ -f $(BONUS_SENT) ]; then \
		$(RM) $(OBJS) $(BONUS_OBJS) $(NAME) $(BONUS_SENT); \
	fi
	@$(MAKE) --no-print-directory $(OBJS)
	$(AR) $(NAME) $(OBJS)
	@touch $(MAND_SENT)

bonus: $(BONUS_SENT)

$(BONUS_SENT):
	@if [ -f $(MAND_SENT) ]; then \
		$(RM) $(OBJS) $(BONUS_OBJS) $(NAME) $(MAND_SENT); \
	fi
	@$(MAKE) --no-print-directory $(BONUS_OBJS)
	$(AR) $(NAME) $(BONUS_OBJS)
	@touch $(BONUS_SENT)

$(OBJS): %.o: %.c ft_printf.h
	$(CC) $(CFLAGS) -c $< -o $@

$(BONUS_OBJS): %.o: %.c ft_printf_bonus.h ft_printf_num_bonus.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS) $(BONUS_OBJS) $(MAND_SENT) $(BONUS_SENT)

fclean: clean
	$(RM) $(NAME)

re: fclean all bonus

.PHONY: all clean fclean re bonus
