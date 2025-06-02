# w.py
Waiter Launcher, n分後に起動するだけのプログラム。

## Demo

### ChatGPT に投げた内容を2分後に見たい場合
![Image](https://github.com/user-attachments/assets/7d007248-0aa8-4739-992d-f60e47d6861d)

コマンド本体だと `python w.py 2 (URL)` だが、ラッパーを工夫すれば、上記のようにファイル名を指定して実行からすぐ実行できるようになる。

### URLとテキストに対応
![Image](https://github.com/user-attachments/assets/8973189b-7798-4df8-993c-7ec2006aec82)

URL の場合は、その URL をブラウザで開く。それ以外の場合はテキストとみなし、テキストファイルに保存した上でそのファイルを開く。つまり利用者目線では「新しいテキストファイルが開かれる」という形でリマインドされる。

## Requirements
- Windows
- Python 3.7+

## How to

### ラッパーのつくりかた
- 1: バッチファイルでくるむ
    - w_wrapper.bat 参照
- 2: 実行時に DOS 窓が出ないようにする
    - w_wrapper.bat のショートカットをつくり、プロパティから実行時のサイズを最小化にする（画像参照）

![Image](https://github.com/user-attachments/assets/d971c114-b531-425b-abd4-2ba2c703d640)

### 今起動してる Waiter を一覧化する
powershell で可能。`-match` の部分でフィルタリングできる。

```
$ powershell -Command "Get-WmiObject Win32_Process | Select-Object Name, CommandLine | Where-Object { $_.CommandLine -match 'w.py' }"
```

## LICENSE
MIT
