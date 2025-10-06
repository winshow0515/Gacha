import RPi.GPIO as GPIO
import time
import subprocess
from mfrc522 import SimpleMFRC522


# ====== GPIO 設定 ======
#REED_PIN = 17  # GPIO17 = Pin 11
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(REED_PIN, GPIO.IN)

# 初始化讀卡機
reader = SimpleMFRC522()


# ====== UID 分類 ======
TYPE_A = {"1016895344656"}
TYPE_B = {"536211394692"}

VIDEO_A = "./video/a.mp4"
VIDEO_B = "./video/b.mp4"
VIDEO_DEFAULT = "./video/default.mp4"


# ====== 工具函式 ======
def play_video(path):
    subprocess.Popen([
        "cvlc",
        "--play-and-exit",
        "--fullscreen",
        "--no-osd",
        path
    ])



# ====== 主流程 ======

try:
    while True:
        print("請將卡片放到讀卡機上...")
        id, text = reader.read()
        uid_str = str(id)  # 轉成字串
        print(f"偵測到 UID: {uid_str}")

        if uid_str in TYPE_A:
            print(f"播放影片:TYPE_A")
            play_video(VIDEO_A)
        elif uid_str in TYPE_B:
            print(f"播放影片:TYPE_B")
            play_video(VIDEO_B)
        else:
            print("未登錄的卡片 UID")
            play_video(VIDEO_DEFAULT)
        time.sleep(1)

except KeyboardInterrupt:
    print("程式結束")
finally:
    GPIO.cleanup()
