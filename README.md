# wait-launcher
Waiter Launcher, n分後に起動するだけのプログラム。

stakiranさんによる[フォーク元](https://github.com/stakiran/w.py)を改善しました。

## 変更点

- 任意のコマンドを実行できるように

## 使い方
`deno -A launch.ts 1 s "タイトル" xdg-open https://www.google.com/`

## Requirements
- OS
    - macOS
    - Linux
    - OSのバージョンは、Deno 2.2.9が動くバージョンならよし
- Deno
  - Deno 2.2.9
- インストールのためのgithub.comへのSSH/HTTPSアクセス
- xterm


## LICENSE
MIT
