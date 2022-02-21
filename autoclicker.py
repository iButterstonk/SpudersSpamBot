import pyautogui
import time


def clicker(cps, button):
    print("Click!")
    pyautogui.click(button=button)
    time.sleep(1/cps)


while True:
    clicker(40, 'left')
