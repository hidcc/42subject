# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hakuta <hakuta@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/25 12:41:44 by hakuta            #+#    #+#              #
#    Updated: 2026/04/25 12:41:47 by hakuta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


NAME		= libgnl.a
BONUS_NAME	= libgnl_bonus.a

CC			= cc
CFLAGS		= -Wall -Wextra -Werror
BUFFER_SIZE	?= 42
DFLAGS		= -D BUFFER_SIZE=$(BUFFER_SIZE)
AR			= ar rcs
RM			= rm -f

SRCS		= get_next_line.c get_next_line_utils.c
OBJS		= $(SRCS:.c=.o)

BONUS_SRCS	= get_next_line_bonus.c get_next_line_utils_bonus.c
BONUS_OBJS	= $(BONUS_SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(AR) $(NAME) $(OBJS)

bonus: $(BONUS_NAME)

$(BONUS_NAME): $(BONUS_OBJS)
	$(AR) $(BONUS_NAME) $(BONUS_OBJS)

%.o: %.c
	$(CC) $(CFLAGS) $(DFLAGS) -c $< -o $@

$(OBJS): get_next_line.h
$(BONUS_OBJS): get_next_line_bonus.h

clean:
	$(RM) $(OBJS) $(BONUS_OBJS)

fclean: clean
	$(RM) $(NAME) $(BONUS_NAME)

re: fclean all

.PHONY: all bonus clean fclean re
