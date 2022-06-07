import argparse
import ctypes
from datetime import datetime
from time import sleep

SCROLLOCK = 0x91


def press_key(user32, key, delay: float):
    user32.keybd_event(key, 0, 0, 0)
    sleep(delay)
    user32.keybd_event(key, 0, 2, 0)


def awake(user32, key, delay: float, count: int, silent: bool):
    for i in range(0, count):
        press_key(user32, key, delay)
        sleep(delay)
    if not silent:
        print(datetime.now().strftime("%H:%M:%S"), ": Hey! Wake up!", sep="")


def check(count: int, delay: float, timespan: int):
    if count < 1:
        print("-c (count) can not be less than 1")
        exit(-1)
    if delay < 0:
        print("-d (delay) can not be less than 0")
        exit(-1)
    if timespan < 1:
        print("-t (timespan) can not be less than 1")
        exit(-1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="This windows-only script is designed to keep the computer powered on without allowing it to go "
                    "into hibernation mode. Unlike AWAKE from PowerToys or the simple power plans settings in "
                    "windows, this \"low-level\" approach bypasses the corporate settings for automatically exit due "
                    "to inactivity",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--count", help="Count of key pressing/releasing actions. "
                                              "Default is 2 (i.e. key presses and then releases two times in a row).",
                        default=2)
    parser.add_argument("-d", "--delay", help="The length of the delay between key pressing/releasing (in seconds). "
                                              "Default value is 0.001",
                        default=0.001)
    parser.add_argument("-k", "--key", help="The code of the key used to perform the \"awake\" action. "
                                            "You can see the key codes here "
                                            "https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes "
                                            "(column \"value\"). Default value is 0x91 (SCROLLOCK)",
                        default=SCROLLOCK)
    parser.add_argument("-s", "--silent",
                        action='store_true',
                        help="Silent execution flag. If present - script will not write log of \"awake\" actions")
    parser.add_argument("-t", "--timespan", help="The length of the time span between \"awake\" actions (in seconds). "
                                                 "Default value is 600 (10 minutes)",
                        default=600)
    parser.add_argument("-ac", "--awake_count",
                        help="Total count of awake actions. E.g. with --timespan=600 and --awake_count=6 script will "
                             "awake your computer ~1 hour. "
                             "Default value is 0 (Will working before manual interrupting "
                             "e.g. Ctrl+C in terminal)",
                        default=0)

    args = vars(parser.parse_args())
    count = int(args.get("count"))
    delay = float(args.get("delay"))
    key = args.get("key")
    silent = bool(args.get("silent"))
    timespan = int(args.get("timespan"))
    awake_count = int(args.get("awake_count"))

    check(count, delay, timespan)
    # -----------
    user32 = ctypes.windll.user32
    awake_left = awake_count
    while True if awake_count <= 0 else awake_left > 0:
        awake(user32, key, delay, count, silent)
        sleep(timespan)
        awake_left -= 1
