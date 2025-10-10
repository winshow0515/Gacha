from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time

def record_uid(file_path):
    reader = SimpleMFRC522()
    print(f"開始記錄 UID 到 {file_path}")
    print("請將卡片一張一張靠近讀卡機，Ctrl+C 結束\n")

    try:
        while True:
            id, text = reader.read()
            uid_str = str(id)
            print(f"偵測到 UID：{uid_str}")

            # 讀取現有檔案，避免重複
            with open(file_path, "a+") as f:
                f.seek(0)
                lines = [line.strip() for line in f.readlines()]
                if uid_str not in lines:
                    f.write(uid_str + "\n")
                    print(f"→ 已寫入 {file_path}")
                else:
                    print("此 UID 已存在，略過")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n結束記錄")
    finally:
        GPIO.cleanup()

def main():
    print("請選擇要記錄的類別：")
    choice = input("輸入 A 或 B：").strip()

    if choice == "A":
        record_uid("uid_a.txt")
    elif choice == "B":
        record_uid("uid_b.txt")
    else:
        print("無效選擇，程式結束")

if __name__ == "__main__":
    main()
