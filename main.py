import RPi.GPIO as GPIO
import time
import subprocess
from mfrc522 import SimpleMFRC522
import os

# ====== 初始化讀卡機 ======
reader = SimpleMFRC522()

# ====== 檔案路徑 ======
FILE_A = "uid_a.txt"
FILE_B = "uid_b.txt"

# ====== 影片路徑 ======
VIDEO_A = "./video/a.mp4"
VIDEO_B = "./video/b.mp4"
VIDEO_DEFAULT = "./video/default.mp4"


# ====== 工具函式 ======
def load_uids(filepath):
    """從文字檔讀取 UID，一行一個"""
    if not os.path.exists(filepath):
        print(f"[警告] 找不到 {filepath}，使用空白清單。")
        return set()
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return set(lines)


def play_video(path):
    subprocess.run([
        "cvlc",
        "--play-and-exit",
        "--fullscreen",
        "--no-osd",
        path
    ])


# ====== 主流程 ======
try:
    # 一開始先載入 UID 清單
    TYPE_A = load_uids(FILE_A)
    TYPE_B = load_uids(FILE_B)

    print("=== UID 名單已載入 ===")
    print(f"TYPE_A: {TYPE_A}")
    print(f"TYPE_B: {TYPE_B}")

    while True:
        print("\n請將卡片放到讀卡機上...")
        id, text = reader.read()
        uid_str = str(id)
        print(f"偵測到 UID: {uid_str}")

        if uid_str in TYPE_A:
            print("播放影片: TYPE_A")
            play_video(VIDEO_A)
        elif uid_str in TYPE_B:
            print("播放影片: TYPE_B")
            play_video(VIDEO_B)
        else:
            print("未登錄的卡片 UID")
            play_video(VIDEO_DEFAULT)

        # 防止重複偵測
        time.sleep(1)

except KeyboardInterrupt:
    print("\n程式結束")
finally:
    GPIO.cleanup()
