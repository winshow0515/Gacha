import os


def play_animation():
    video_path = r"C:\Users\winsh\Desktop\Gacha_machine\example.mp4"
    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"

    os.system(
        f'start /B "" "{vlc_path}" '
        f'--play-and-exit --fullscreen --no-video-deco --no-embedded-video --qt-start-minimized "{video_path}"'
    )

print("請按 Enter 模擬扭蛋觸發動畫...")
while True:
    input()  # 等待用戶按下 Enter 鍵
    play_animation()  # 播放動畫
    print("請按 Enter 模擬扭蛋觸發動畫...")