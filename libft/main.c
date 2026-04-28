#include "libft.h"
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <unistd.h>

static char	to_upper_map(unsigned int i, char c)
{
	(void)i;
	if (c >= 'a' && c <= 'z')
		return (c - 32);
	return (c);
}

static void	ft_putendl_fd_wrapper(void *s)
{
	ft_putendl_fd((char *)s, 1);
}

static void	*dup_content(void *content)
{
	return (ft_strdup((char *)content));
}

static void	to_upper_iter(unsigned int i, char *c)
{
	(void)i;
	if (*c >= 'a' && *c <= 'z')
		*c -= 32;
}

int	main(void)
{
	char	b1[10] = "abcdefghi";
	char	b2[10] = "abcdefghi";
	char	b3[10] = "abcdefghi";
	char	b4[10] = "abcdefghi";
	char	b5[10] = "abcdefghi";
	char	b6[10] = "abcdefghi";
	char	cpy_fwd[10] = "abcdefghi";
	char	mov_fwd[10] = "abcdefghi";
	char	cpy_bwd[10] = "abcdefghi";
	char	mov_bwd[10] = "abcdefghi";
	char	*tmp;
	char	buf_sc[10];
	char	buf_slc[20];
	int		*arr;
	char	**sp;
	int		i;
	char	iter_buf[] = "hello";

	printf("=== ft_isalpha ===\n");
	printf("'A': %d\n", ft_isalpha('A'));
	printf("'z': %d\n", ft_isalpha('z'));
	printf("'0': %d\n", ft_isalpha('0'));
	printf("' ': %d\n", ft_isalpha(' '));
	printf("'@': %d\n", ft_isalpha('@'));
	printf("127: %d\n", ft_isalpha(127));
	printf("0:   %d\n", ft_isalpha(0));

	printf("=== ft_isdigit ===\n");
	printf("'A': %d\n", ft_isdigit('A'));
	printf("'z': %d\n", ft_isdigit('z'));
	printf("'0': %d\n", ft_isdigit('0'));
	printf("' ': %d\n", ft_isdigit(' '));
	printf("'@': %d\n", ft_isdigit('@'));
	printf("127: %d\n", ft_isdigit(127));
	printf("0:   %d\n", ft_isdigit(0));

	printf("=== ft_isalnum ===\n");
	printf("'A': %d\n", ft_isalnum('A'));
	printf("'z': %d\n", ft_isalnum('z'));
	printf("'0': %d\n", ft_isalnum('0'));
	printf("' ': %d\n", ft_isalnum(' '));
	printf("'@': %d\n", ft_isalnum('@'));
	printf("127: %d\n", ft_isalnum(127));
	printf("0:   %d\n", ft_isalnum(0));

	printf("=== ft_isascii ===\n");
	printf("'A': %d\n", ft_isascii('A'));
	printf("'z': %d\n", ft_isascii('z'));
	printf("'0': %d\n", ft_isascii('0'));
	printf("' ': %d\n", ft_isascii(' '));
	printf("'@': %d\n", ft_isascii('@'));
	printf("127: %d\n", ft_isascii(127));
	printf("0:   %d\n", ft_isascii(0));

	printf("=== ft_isprint ===\n");
	printf("'A': %d\n", ft_isprint('A'));
	printf("'z': %d\n", ft_isprint('z'));
	printf("'0': %d\n", ft_isprint('0'));
	printf("' ': %d\n", ft_isprint(' '));
	printf("'@': %d\n", ft_isprint('@'));
	printf("127: %d\n", ft_isprint(127));
	printf("0:   %d\n", ft_isprint(0));

	printf("=== ft_strlen ===\n");
	printf("hello:     %zu\n", ft_strlen("hello"));
	printf("(empty):   %zu\n", ft_strlen(""));
	printf("a:         %zu\n", ft_strlen("a"));
	printf("hello\\0xx: %zu\n", ft_strlen("hello\0xx"));

	printf("=== ft_toupper / ft_tolower ===\n");
	printf("toupper('a'): %c\n", ft_toupper('a'));
	printf("toupper('A'): %c\n", ft_toupper('A'));
	printf("toupper('1'): %c\n", ft_toupper('1'));
	printf("tolower('Z'): %c\n", ft_tolower('Z'));
	printf("tolower('z'): %c\n", ft_tolower('z'));
	printf("tolower('!'): %c\n", ft_tolower('!'));

	printf("=== ft_memset ===\n");
	ft_memset(b1, 'X', 5);
	printf("('X', 5): %s\n", b1);
	ft_memset(b1, 'Y', 9);
	printf("('Y', 9): %s\n", b1);
	ft_memset(b1, 'Z', 0);
	printf("('Z', 0): %s\n", b1);

	printf("=== ft_bzero ===\n");
	ft_bzero(b2, 5);
	printf("(5): [%d,%d,%d,%d,%d,%c,%c,%c,%c]\n",
		b2[0], b2[1], b2[2], b2[3], b2[4], b2[5], b2[6], b2[7], b2[8]);
	ft_bzero(b2, 9);
	printf("(9): [%d,%d,%d,%d,%d,%d,%d,%d,%d]\n",
		b2[0], b2[1], b2[2], b2[3], b2[4], b2[5], b2[6], b2[7], b2[8]);
	ft_bzero(b2, 0);
	printf("(0): [%d]\n", b2[0]);

	printf("=== ft_memcpy ===\n");
	ft_memcpy(b3, "XXXXX", 5);
	printf("(XXXXX, 5): %s\n", b3);
	ft_memcpy(b3, "123456789", 9);
	printf("(123456789, 9): %s\n", b3);
	ft_memcpy(b3, "ABC", 0);
	printf("(ABC, 0): %s\n", b3);
	printf("(NULL,NULL,0): %p\n", ft_memcpy(NULL, NULL, 0));

	printf("=== ft_memmove ===\n");
	ft_memmove(b4 + 2, b4, 5);
	printf("forward overlap (dst+2, src, 5): %s\n", b4);
	ft_memmove(b5, b5 + 2, 5);
	printf("backward overlap (dst, src+2, 5): %s\n", b5);
	ft_memmove(b6, b6, 0);
	printf("n=0:                         %s\n", b6);
	printf("(NULL,NULL,0): %p\n", ft_memmove(NULL, NULL, 0));

	printf("=== ft_memcpy vs ft_memmove ===\n");
	ft_memcpy(cpy_fwd + 2, cpy_fwd, 5);
	ft_memmove(mov_fwd + 2, mov_fwd, 5);
	printf("forward overlap (dst+2, src, 5):\n");
	printf("  memcpy:  %s\n", cpy_fwd);
	printf("  memmove: %s\n", mov_fwd);
	ft_memcpy(cpy_bwd, cpy_bwd + 2, 5);
	ft_memmove(mov_bwd, mov_bwd + 2, 5);
	printf("backward overlap (dst, src+2, 5):\n");
	printf("  memcpy:  %s\n", cpy_bwd);
	printf("  memmove: %s\n", mov_bwd);

	printf("=== ft_strlcpy ===\n");
	printf("ret=%zu ", ft_strlcpy(buf_sc, "hello", 10));
	printf("dst=%s\n", buf_sc);
	printf("ret=%zu ", ft_strlcpy(buf_sc, "hello world!", 5));
	printf("dst=%s\n", buf_sc);
	printf("dsize=0: ret=%zu\n", ft_strlcpy(buf_sc, "test", 0));

	printf("=== ft_strlcat ===\n");
	ft_strlcpy(buf_slc, "Hello", 20);
	printf("ret=%zu ", ft_strlcat(buf_slc, " World", 20));
	printf("dst=%s\n", buf_slc);
	ft_strlcpy(buf_slc, "Hello", 20);
	printf("ret=%zu ", ft_strlcat(buf_slc, " World", 8));
	printf("dst=%s\n", buf_slc);
	ft_strlcpy(buf_slc, "Hello", 20);
	printf("dsize=0:   ret=%zu\n", ft_strlcat(buf_slc, " World", 0));
	ft_strlcpy(buf_slc, "Hi", 20);
	printf("dsize<dst: ret=%zu\n", ft_strlcat(buf_slc, " World", 1));
	ft_strlcpy(buf_slc, "", 20);
	printf("ret=%zu ", ft_strlcat(buf_slc, "World", 20));
	printf("dst=%s\n", buf_slc);
	ft_strlcpy(buf_slc, "Hello", 20);
	printf("ret=%zu ", ft_strlcat(buf_slc, "", 20));
	printf("dst=%s\n", buf_slc);

	printf("=== ft_strchr ===\n");
	printf("'l' in hello: %s\n", ft_strchr("hello", 'l'));
	printf("'z' in hello: %s\n", ft_strchr("hello", 'z'));
	printf("'\\0' in hi:  found=%d\n", ft_strchr("hi", '\0') != NULL);
	printf("'h' in (empty): %s\n", ft_strchr("", 'h'));

	printf("=== ft_strrchr ===\n");
	printf("'l' in hello:   %s\n", ft_strrchr("hello", 'l'));
	printf("'z' in hello:   %s\n", ft_strrchr("hello", 'z'));
	printf("'\\0' in hi:    found=%d\n", ft_strrchr("hi", '\0') != NULL);
	printf("'o' in bonjour: %s\n", ft_strrchr("bonjour", 'o'));

	printf("=== ft_strncmp ===\n");
	printf("abc vs abd (3): %d\n", ft_strncmp("abc", "abd", 3));
	printf("abc vs abc (3): %d\n", ft_strncmp("abc", "abc", 3));
	printf("abc vs abd (2): %d\n", ft_strncmp("abc", "abd", 2));
	printf("n=0: %d\n", ft_strncmp("abc", "xyz", 0));
	printf("(empty) vs a (1): %d\n", ft_strncmp("", "a", 1));
	printf("unsigned: %d\n", ft_strncmp("\200", "\0", 1) > 0);

	printf("=== ft_memchr ===\n");
	printf("('a', 9): %s\n", (char *)ft_memchr("abcdefghi", 'a', 9));
	printf("('e', 9): %s\n", (char *)ft_memchr("abcdefghi", 'e', 9));
	printf("('i', 9): %s\n", (char *)ft_memchr("abcdefghi", 'i', 9));

	printf("=== ft_memcmp ===\n");
	printf("vs abcdefghi (9): %d\n",
		ft_memcmp("abcdefghi", "abcdefghi", 9));
	printf("vs abcdefghX (9): %d\n",
		ft_memcmp("abcdefghi", "abcdefghX", 9));
	printf("vs Xbcdefghi (9): %d\n",
		ft_memcmp("abcdefghi", "Xbcdefghi", 9));
	printf("vs xxxxxxxxx (0): %d\n",
		ft_memcmp("abcdefghi", "xxxxxxxxx", 0));

	printf("=== ft_strnstr ===\n");
	printf("lo in hello (5): %s\n", ft_strnstr("hello", "lo", 5));
	printf("lo in hello (3): %s\n", ft_strnstr("hello", "lo", 3));
	printf("empty needle: %s\n", ft_strnstr("hello", "", 5));
	printf("needle > hay: %s\n", ft_strnstr("hi", "hello", 5));
	printf("n=0: %s\n", ft_strnstr("hello", "lo", 0));

	printf("=== ft_atoi ===\n");
	printf("100:        %d\n", ft_atoi("100"));
	printf("-100:       %d\n", ft_atoi("-100"));
	printf("  +100:     %d\n", ft_atoi("  +100"));
	printf("+-100:      %d\n", ft_atoi("+-100"));
	printf("100abc:     %d\n", ft_atoi("100abc"));
	printf("(empty):    %d\n", ft_atoi(""));
	printf("INT_MAX:    %d\n", ft_atoi("2147483647"));
	printf("INT_MIN:    %d\n", ft_atoi("-2147483648"));

	printf("=== ft_calloc ===\n");
	arr = (int *)ft_calloc(3, sizeof(int));
	printf("[%d, %d, %d]\n", arr[0], arr[1], arr[2]);
	free(arr);

	printf("=== ft_strdup ===\n");
	tmp = ft_strdup("hello");
	printf("%s\n", tmp);
	free(tmp);
	tmp = ft_strdup("");
	printf("empty: %s\n", tmp);
	free(tmp);

	printf("=== ft_substr ===\n");
	tmp = ft_substr("hello world", 6, 5);
	printf("%s\n", tmp);
	free(tmp);
	tmp = ft_substr("hello", 0, 3);
	printf("start=0: %s\n", tmp);
	free(tmp);
	tmp = ft_substr("hello", 10, 5);
	printf("start>len: %s\n", tmp);
	free(tmp);
	tmp = ft_substr("", 0, 5);
	printf("empty: %s\n", tmp);
	free(tmp);

	printf("=== ft_strjoin ===\n");
	tmp = ft_strjoin("Hello ", "World");
	printf("%s\n", tmp);
	free(tmp);

	printf("=== ft_strtrim ===\n");
	tmp = ft_strtrim("  Hello  ", " ");
	printf("%s\n", tmp);
	free(tmp);
	tmp = ft_strtrim("xxHelloxx", "x");
	printf("%s\n", tmp);
	free(tmp);
	tmp = ft_strtrim("aaa", "a");
	printf("%s\n", tmp);
	free(tmp);

	printf("=== ft_split ===\n");
	printf("hello world ' ':\n");
	sp = ft_split("hello world ", ' ');
	i = 0;
	while (sp[i])
	{
		printf("%s\n", sp[i]);
		free(sp[i]);
		i++;
	}
	free(sp);

	printf("  hello  world   ' ':\n");
	sp = ft_split("  hello  world  ", ' ');
	i = 0;
	while (sp[i])
	{
		printf("%s\n", sp[i]);
		free(sp[i]);
		i++;
	}
	free(sp);

	printf("=== ft_itoa ===\n");
	tmp = ft_itoa(100);
	printf("100:    %s\n", tmp);
	free(tmp);
	tmp = ft_itoa(-100);
	printf("-100:   %s\n", tmp);
	free(tmp);
	tmp = ft_itoa(0);
	printf("0:     %s\n", tmp);
	free(tmp);
	tmp = ft_itoa(INT_MIN);
	printf("MIN:   %s\n", tmp);
	free(tmp);
	tmp = ft_itoa(INT_MAX);
	printf("MAX:   %s\n", tmp);
	free(tmp);

	printf("=== ft_strmapi ===\n");
	tmp = ft_strmapi("hello", to_upper_map);
	printf("%s\n", tmp);
	free(tmp);
	tmp = ft_strmapi("", to_upper_map);
	printf("empty: %s\n", tmp);
	free(tmp);

	printf("=== ft_striteri ===\n");
	ft_striteri(iter_buf, to_upper_iter);
	printf("%s\n", iter_buf);

	printf("=== ft_putchar_fd ===\n");
	ft_putchar_fd('A', 1);
	ft_putchar_fd('\n', 1);

	printf("=== ft_putstr_fd ===\n");
	ft_putstr_fd("Hello", 1);
	ft_putstr_fd("\n", 1);

	printf("=== ft_putendl_fd ===\n");
	ft_putendl_fd("with newline", 1);

	printf("=== ft_putnbr_fd ===\n");
	ft_putnbr_fd(0, 1);
	write(1, "\n", 1);
	ft_putnbr_fd(100, 1);
	write(1, "\n", 1);
	ft_putnbr_fd(-100, 1);
	write(1, "\n", 1);
	ft_putnbr_fd(INT_MAX, 1);
	write(1, "\n", 1);
	ft_putnbr_fd(INT_MIN, 1);
	write(1, "\n", 1);

	printf("=== ft_lstnew ===\n");
	{
		t_list	*node = ft_lstnew("hello");
		printf("content: %s\n", (char *)node->content);
		printf("next: %p\n", (void *)node->next);
		free(node);
	}

	printf("=== ft_lstadd_front ===\n");
	{
		t_list	*lst = NULL;
		t_list	*n1 = ft_lstnew("second");
		t_list	*n2 = ft_lstnew("first");
		ft_lstadd_front(&lst, n1);
		ft_lstadd_front(&lst, n2);
		printf("head: %s\n", (char *)lst->content);
		printf("next: %s\n", (char *)lst->next->content);
		free(n1);
		free(n2);
	}

	printf("=== ft_lstsize ===\n");
	{
		t_list	*lst = NULL;
		t_list	*n1 = ft_lstnew("a");
		t_list	*n2 = ft_lstnew("b");
		t_list	*n3 = ft_lstnew("c");
		ft_lstadd_front(&lst, n1);
		ft_lstadd_front(&lst, n2);
		ft_lstadd_front(&lst, n3);
		printf("size=3: %d\n", ft_lstsize(lst));
		printf("size=0: %d\n", ft_lstsize(NULL));
		free(n1);
		free(n2);
		free(n3);
	}

	printf("=== ft_lstlast ===\n");
	{
		t_list	*lst = NULL;
		t_list	*n1 = ft_lstnew("first");
		t_list	*n2 = ft_lstnew("last");
		ft_lstadd_front(&lst, n2);
		ft_lstadd_front(&lst, n1);
		printf("last: %s\n", (char *)ft_lstlast(lst)->content);
		printf("NULL: %p\n", (void *)ft_lstlast(NULL));
		free(n1);
		free(n2);
	}

	printf("=== ft_lstadd_back ===\n");
	{
		t_list	*lst = NULL;
		t_list	*n1 = ft_lstnew("first");
		t_list	*n2 = ft_lstnew("last");
		ft_lstadd_back(&lst, n1);
		ft_lstadd_back(&lst, n2);
		printf("head: %s\n", (char *)lst->content);
		printf("tail: %s\n", (char *)ft_lstlast(lst)->content);
		free(n1);
		free(n2);
	}

	printf("=== ft_lstdelone ===\n");
	{
		t_list	*node = ft_lstnew(ft_strdup("delete me"));
		ft_lstdelone(node, free);
		printf("done\n");
	}

	printf("=== ft_lstclear ===\n");
	{
		t_list	*lst = NULL;
		ft_lstadd_back(&lst, ft_lstnew(ft_strdup("a")));
		ft_lstadd_back(&lst, ft_lstnew(ft_strdup("b")));
		ft_lstadd_back(&lst, ft_lstnew(ft_strdup("c")));
		ft_lstclear(&lst, free);
		printf("cleared: %p\n", (void *)lst);
	}

	printf("=== ft_lstiter ===\n");
	{
		t_list	*lst = NULL;
		ft_lstadd_back(&lst, ft_lstnew(ft_strdup("hello")));
		ft_lstadd_back(&lst, ft_lstnew(ft_strdup("world")));
		ft_lstiter(lst, (void (*)(void *))ft_putendl_fd_wrapper);
		ft_lstclear(&lst, free);
	}

	printf("=== ft_lstmap ===\n");
	{
		t_list	*lst = NULL;
		t_list	*mapped;
		t_list	*cur;
		ft_lstadd_back(&lst, ft_lstnew(ft_strdup("hello")));
		ft_lstadd_back(&lst, ft_lstnew(ft_strdup("world")));
		mapped = ft_lstmap(lst, dup_content, free);
		cur = mapped;
		while (cur)
		{
			printf("%s\n", (char *)cur->content);
			cur = cur->next;
		}
		ft_lstclear(&lst, free);
		ft_lstclear(&mapped, free);
	}

	return (0);
}
