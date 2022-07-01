import keyboard
import time


def main():
    while keyboard.is_pressed("a"):
        print("yeah baby! ")
        time.sleep(1)


if __name__=='__main__':
    while True:
        main()

