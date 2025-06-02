import sys
import time
import webbrowser
import os
import random
import string

def generate_random_filename():
    # 3桁のランダムな大文字の英字または数字を生成
    return 'remind' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) + '.txt'

def open_in_editor(filename):
    if os.name == 'nt':  # Windowsの場合
        os.startfile(filename)
    elif sys.platform == 'darwin':  # macOSの場合
        os.system(f'open {filename}')
    else:  # その他のUNIX系OSの場合
        os.system(f'xdg-open {filename}')

def main():
    if len(sys.argv) < 3:
        print("Usage: w.py (wait_time_in_minutes) (command_line)")
        sys.exit(1)
    
    wait_time = int(sys.argv[1])
    command_line = ' '.join(sys.argv[2:])
    print(f"{command_line}")

    # 待ち時間（分）を秒に変換
    wait_seconds = wait_time * 60
    print(f"Waiting for {wait_time} minute(s)...")
    time.sleep(wait_seconds)

    if command_line.startswith("http://") or command_line.startswith("https://"):
        # URLの場合、ブラウザで開く
        webbrowser.open(command_line)
    else:
        # それ以外の場合、remindXXX.txt に書き込んでから開く
        filename = generate_random_filename()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(command_line)
        
        open_in_editor(filename)

if __name__ == '__main__':
    main()
