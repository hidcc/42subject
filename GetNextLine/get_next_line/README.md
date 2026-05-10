*This project has been created as part of the 42 curriculum by hakuta.*

# get_next_line

## Description（概要）

`get_next_line` は、ファイルディスクリプタから **1行ずつ** 読み取って返す関数を実装する課題です。関数を繰り返し呼ぶことで、ファイルの内容を 1 行ずつ取り出していきます。読み取った行には終端の `\n` を含めます（ただしファイルが `\n` で終わっていない最終行を除く）。読み終えた場合やエラー発生時は `NULL` を返します。

### プロトタイプ

```c
char *get_next_line(int fd);
```

- **引数** — `fd`: 読み取り対象のファイルディスクリプタ
- **戻り値** — 読み取った行、またはエラー時／読み終えた時は `NULL`
- **使用可能な外部関数** — `read`, `malloc`, `free`
- **禁止事項** — `libft`、`lseek`、グローバル変数

## Instructions（使い方）

### ファイル構成

- `get_next_line.c`  `get_next_line()` 本体のロジック
- `get_next_line_utils.c`  補助関数群（`ft_strlen`, `ft_strchr`, `ft_strjoin_free`, `ft_extract_line`, `ft_update_stash`）
- `get_next_line.h`  プロトタイプ・インクルード・`BUFFER_SIZE` のデフォルト値を定義するヘッダ

### コンパイル

`-D BUFFER_SIZE` フラグの **あり／なしの両方** でコンパイルできる必要があります。ヘッダ側でデフォルト値（42）を用意しています。

```
# デフォルトの BUFFER_SIZE（42）でコンパイル
cc -Wall -Wextra -Werror get_next_line.c get_next_line_utils.c main.c -o gnl

# BUFFER_SIZE を指定してコンパイル
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c main.c -o gnl
```

### 使用例

`test.txt` の内容（各行末は改行）：

```
hello
world
42tokyo
```

呼び出し側のコード例：

```c
#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

int main(void)
{
    int   fd = open("test.txt", O_RDONLY);
    char *line;

    while ((line = get_next_line(fd)) != NULL)
    {
        printf("%s", line);
        free(line);
    }
    close(fd);
    return (0);
}
```

標準入力（`fd = 0`）からの読み取りにも対応しています。

## Algorithm（アルゴリズム）

`get_next_line()` の内部には、呼び出しをまたいで生き残る `static char *stash`（残骸バッファ）が 1 つだけあります。`read()` で読み取ったが、まだ呼び出し元へ返していない文字をここに溜め込みます。

1 回の `get_next_line()` 呼び出しは、次の 3 ステップで進みます。

1. **改行が見つかるまで stash を満たす**
   `read_until_newline()` が `read(fd, buf, BUFFER_SIZE)` を繰り返し、読み取ったチャンクを `ft_strjoin_free()` で stash に連結していきます。`ft_strjoin_free()` は連結後に古い stash を `free` するため、リークが起きません。stash に `\n` が含まれた時点、`read()` が `0`（EOF）を返した時点、`-1`（エラー）を返した時点で停止します。エラー時は stash を解放して `NULL` を返します。

2. **行を切り出す**
   `ft_extract_line()` が stash の先頭から最初の `\n` までをコピーします（`\n` を含む）。EOF まで到達して `\n` が無かった場合は、stash の末尾までをコピーします。これが呼び出し元へ返される文字列です。

3. **stash を更新する**
   `ft_update_stash()` が、最初の `\n` より後ろを新しい stash として作り直します。残りが空であれば stash を解放して `NULL` に戻し、次回呼び出しに備えます。

### 設計の根拠

- **必要な分だけ読む**
  subject に「ファイル全体を一度に読んでから処理してはならない」と明記されています。`\n` が見つかった瞬間にループを抜けるので、本当に必要なチャンクだけを `read()` します。
- **任意の `BUFFER_SIZE` に対して堅牢**
  `BUFFER_SIZE` が 1 でも 9999 でも 10000000 でも、ロジックは同じです（チャンクを読み、連結し、`\n` を探す）。エントリポイントで `BUFFER_SIZE <= 0` の場合は `NULL` を返してガードしています。
- **メモリリークを起こさない**
  すべての確保に明確な所有者がいます。`ft_strjoin_free()` は左辺の文字列を解放し、`read_until_newline()` の一時バッファ `buf` は関数末尾で解放、`read()` がエラーを返した場合は stash を解放してから `NULL` を返します。
- **グローバル変数ではなく static 変数を使う**
  読み取り状態は `get_next_line()` 内部の `static` に置いています。「グローバル変数禁止」のルールを守りつつ、呼び出し間で状態を引き継げます。

### 対応しているエッジケース

- 不正な入力（`fd < 0` または `BUFFER_SIZE <= 0`）→ `NULL` を返す
- `read()` が `-1` を返した場合 → stash を解放して `NULL` を返す
- ファイルが `\n` で終わっていない場合 → 最終行を `\n` 無しで返す
- 空ファイル／EOF 到達 → `NULL` を返し、stash をクリア
- 標準入力（`fd = 0`）→ 同じロジックで動作

## Resources（参考資料）

実装にあたって参照した古典的な資料：

- `man 2 read`
- 42 Tokyo の同期や先輩などからの意見

### AI の使用について

AI ツールは **実装そのものを生成するためには使わず**、補助的な目的に限定して使用しました。

- **subject の読解** — `\n` で終わらない最終行の挙動など、文面で曖昧だった箇所の確認
- **提出前の復習** — `static` 変数や `\n` 周りの自分の理解を言語化するための壁打ち

