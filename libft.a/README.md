*This project has been created as part of the 42 curriculum by hakuta.*

# libft

## Description

C の標準ライブラリ関数や独自ユーティリティ関数を自分で再実装した静的ライブラリ `libft.a`。以降のすべての C プロジェクトで再利用する基盤となる。

### Part 1 — Libc functions (23)

関数を再実装したもの。仕様は man ページに準拠。

`ft_isalpha` `ft_isdigit` `ft_isalnum` `ft_isascii` `ft_isprint`
`ft_toupper` `ft_tolower`
`ft_memset` `ft_bzero` `ft_memcpy` `ft_memmove` `ft_memchr` `ft_memcmp` `ft_calloc`
`ft_strlen` `ft_strlcpy` `ft_strlcat` `ft_strchr` `ft_strrchr` `ft_strncmp` `ft_strnstr` `ft_strdup`
`ft_atoi`

### Part 2 — Additional functions (11)

`ft_substr`
	文字列sのstartから最大len文字を切り出した新しい文字列を返す

`ft_strjoin`
	s1とs2を連結した新しい文字列を返す

`ft_strtrim`
	s1の先頭と末尾からsetに含まれる文字を除いた文字列を返す

`ft_split`
	文字列sを区切り文字cで分割し、NULL終端された文字列配列を返す

`ft_itoa`
	int nを表す文字列を返す

`ft_strmapi`
	sの各文字に関数fを適用した新しい文字列を返す

`ft_striteri`
	sの各文字に関数fを適用する（アドレス渡しで変更可能）

`ft_putchar_fd`
	文字cをfdに出力する

`ft_putstr_fd`
	文字列sをfdに出力する

`ft_putendl_fd`
	文字列sをfdに出力し、末尾に改行を付ける

`ft_putnbr_fd`
	整数nをfdに出力する

### Part 3 — Linked list (9)

t_list構造体を使った単方向連結リスト操作。

typedef struct s_list
{
    void            *content;
    struct s_list   *next;
}   t_list;

`ft_lstnew`
	contentを内容とする新しいノードを作成する

`ft_lstadd_front`
	リスト先頭にnewを追加する

`ft_lstsize`
	リストのノード数を返す

`ft_lstlast`
	リストの末尾ノードを返す

`ft_lstadd_back`
	リスト末尾にnewを追加する

`ft_lstdelone`
	1ノードの内容をdelで解放し、ノード自身も解放する

`ft_lstclear`
	リスト全ノードをdelとfreeで解放する

`ft_lstiter`
	各ノードの内容に関数fを適用する

`ft_lstmap`
	各ノードにfを適用した新しいリストを返す

## Instructions

make          # libft.a を作成
make clean    # .o ファイルを削除
make fclean   # libft.a も削除
make re       # fclean + make

使用時は `#include "libft.h"` して `libft.a` をリンクする。

## Resources

### 参考資料

- man pages

### AI の使用について

- 使用した AI:chat gpt
- 使用したタスク / 部分:勉強の方針建てと復習をした
- 直接コードを書かせた部分（あれば）:コードの修正を手伝ってもらったがコードは自分で書いた
