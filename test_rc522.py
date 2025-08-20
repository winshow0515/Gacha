from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

def main():
    
    reader = SimpleMFRC522()
    print("請把卡片靠近讀卡機...")

    try:
        id, text = reader.read()
        print(f"讀到卡片 UID：{id}")
        if text:
            print(f"卡片內容：{text}")
        else:
            print("卡片沒有內容")
    finally:
        print("結束測試")
        GPIO.cleanup()
if __name__ == "__main__":
    main()
