import RPi.GPIO as GPIO
import time
import subprocess
from mfrc522 import MFRC522


# ====== GPIO 設定 ======
REED_PIN = 17  # GPIO17 = Pin 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(REED_PIN, GPIO.IN)


# ====== RC522 設定 ======
PIN_RST = 25       # GPIO25 = Pin 22
SPI_BUS = 0
SPI_DEV = 0        # 如果 SDA 接 CE1 (Pin 26)，改成 1

reader = MFRC522(bus=SPI_BUS, device=SPI_DEV, pin_rst=PIN_RST)


# ====== UID 分類 ======
TYPE_A = {""}
TYPE_B = {""}

VIDEO_A = "/home/pi/Desktop/Gacha/video/a.mp4"
VIDEO_B = "/home/pi/Desktop/Gacha/video/b.mp4"

delaySec = 0.1


def destroy():
    GPIO.cleanup()


def startReed():
    prev_input = 1
    while True:
        input_result = GPIO.input(REED_PIN)
        if input_result == 0 and prev_input == 1:
            print("Button Pressed")
            play_animation()
            time.sleep(11) #避免重複觸發
        prev_input = input_result
        print(input_result)
        time.sleep(delaySec)

def play_animation(path):
    subprocess.Popen([
        "cvlc",
        "--play-and-exit",
        "--fullscreen",
        "--no-osd",
        path
    ])



if __name__ == "__main__":
    try:
        startReed()
    except KeyboardInterrupt:
        destroy()