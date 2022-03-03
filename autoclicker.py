import pyautogui
import time


def clicker(cps, button):
    print("Click!")
    pyautogui.click(button=button)


while True:
    clicker(40, 'left')
