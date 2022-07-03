import keyboard
import time
import sys
import os


def main():
    while keyboard.is_pressed("a"):

        print("yeah baby! ")
        time.sleep(0.8)


if __name__=='__main__':
    # This prevents keyboard strokes to be printed on to the terminal.
    os.system("stty -echo")
    
    while True:
        try:
            main()
        except KeyboardInterrupt:
            # re-enable keyboard strokes to be printed on to the terminal
            os.system("stty echo")
            if input("Are you sure that you want to quit? (y/n) ").lower() == "y":
                sys.exit(0)
            else:
                os.system("stty -echo")

