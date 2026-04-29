*This project has been created as part of the 42 curriculum by hakuta.*

# ft_printf

## Description

`ft_printf` は標準ライブラリの `printf(3)` を再実装する 42 のプロジェクトです。
C の **可変長引数 (variadic functions)** をしようして実装しています。

実装している変換指定子は以下のとおりです (`cspdiuxX%`)。

`%c`  1文字
`%s`  文字列 (`NULL` のときは `(null)`)
`%p`  `void *` を 16進で表示 (`0x` プレフィックス付)
`%d` `%i` 10進符号付き整数
`%u`  10進符号なし整数
`%x`  16進小文字
`%X`  16進大文字
`%%`　パーセント記号

戻り値は **書き出したバイト数** (失敗時 `-1`) で、本家 `printf` と同じセマンティクスです。
バッファリングは行わず、`write(2)` を直接呼びます (subject の指示)。

## Instructions

### ビルド

```
make            # libftprintf.a を生成
make clean      # オブジェクトファイルを削除
make fclean     # オブジェクト + ライブラリを削除
make re         # fclean + all
```

コンパイルフラグは `-Wall -Wextra -Werror`、アーカイブは `ar rcs` を使用しています。

### 使い方

ヘッダをインクルードしてライブラリをリンクします。

```
#include "ft_printf.h"

int main(void)
{
    ft_printf("c=%c s=%s p=%p d=%d i=%i u=%u x=%x X=%X %%\n",
              'A', "hello", (void *)0, -42, 42, 4294967295u, 255, 255);
    return (0);
}
```

```
cc -Wall -Wextra -Werror main.c libftprintf.a -o main
./main
```

期待出力:
```
c=A s=hello p=(nil) d=-42 i=42 u=4294967295 x=ff X=FF %
```


## アルゴリズムとデータ構造

### 全体設計 — ディスパッチ方式

`ft_printf` 本体 はフォーマット文字列を 1 文字ずつ走査し、`%` を見つけたら次の 1 文字を `print_format()` に渡してディスパッチするという素直な構造にしました。

- **書き出しバイト数の積算**: 各 helper は「成功時に書いたバイト数」「失敗時 `-1`」を返す統一インターフェイスにし、上位で `count += ret` するだけで合計が取れるようにしています。これにより `write` の戻り値検査も自然に伝播します。

### 数値出力 — 再帰による基数変換

`ft_putunbr_base(unsigned long n, char *base)` を `%d` `%i` `%u` `%x` `%X` `%p` の **共通基盤** として使っています。

- **再帰を選んだ理由**: 数値を上位桁から出力するには通常「バッファに逆順で書き込んで反転」する必要がありますが、再帰呼び出しのコールスタックがそのまま順序反転として働くため、**追加のバッファ (= `malloc` または固定長配列)** が不要になります。`unsigned long` の最大桁でも再帰深度はたかだか 64 程度で、スタック消費は無視できる規模です。
- **`unsigned long` で受ける理由**: `%d` の `INT_MIN` を負号反転するときに `int` のままだとオーバーフローします。`long` に昇格してから `-nb` を取り、その後 `unsigned long` にキャストすることで未定義動作を避けています。
- **`%p` での再利用**: ポインタは `unsigned long` にキャストして同じ `ft_putunbr_base` に流すだけで実装できます。`0x` プレフィックスは `ft_putstr` で先に出してから本体を呼ぶ形 (`ft_printf_nbr.c:68-80`)。

### エラー伝播

`write(2)` が失敗した場合に途中までの出力を「成功」と偽らないよう、すべての helper は `-1` を上位へ伝播させ、`ft_printf` 本体も `-1` を返して `va_end` を必ず呼びます。

## Resources

- `man printf`
- `man stdarg`

### AI の利用について

- **使ったところ**: 勉強の方針建てと復習で利用しました。