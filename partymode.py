
import pyautogui
import time

inputNumber = int(input("How many times do you want to spam? "))


def partyBot(input):
    time.sleep(5)
    for i in range(input):
        pyautogui.typewrite("H")


partyBot(inputNumber)
pyautogui.press("enter")
