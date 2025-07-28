import RPi.GPIO as GPIO
import time


reed_button = 17  # GPIO17 = Pin 11
delaySec = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(reed_button, GPIO.IN)


def destroy():
    GPIO.cleanup()


def showResult():
    prev_input = 1
    while True:
        input_result = GPIO.input(reed_button)
        if input_result == 0 and prev_input == 1:
            print("Button Pressed")
            time.sleep(2) #避免重複觸發
        prev_input = input_result
        print(input_result)
        time.sleep(delaySec)


if __name__ == "__main__":
    try:
        showResult()
    except KeyboardInterrupt:
        destroy()