import RPi.GPIO as GPIO
import time
import subprocess


reed_button = 17  # GPIO17 = Pin 11
delaySec = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(reed_button, GPIO.IN)

vedio_path = "./example.mp4"

def destroy():
    GPIO.cleanup()


def startReed():
    prev_input = 1
    while True:
        input_result = GPIO.input(reed_button)
        if input_result == 0 and prev_input == 1:
            print("Button Pressed")
            play_animation()
            time.sleep(11) #避免重複觸發
        prev_input = input_result
        print(input_result)
        time.sleep(delaySec)

def play_animation():
    subprocess.Popen([
        "cvlc",
        "--play-and-exit",
        "--fullscreen",
        "--no-osd",
        vedio_path
    ])



if __name__ == "__main__":
    try:
        startReed()
    except KeyboardInterrupt:
        destroy()