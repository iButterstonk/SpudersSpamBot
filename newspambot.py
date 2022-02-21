import pyautogui
import time


def spamBot():
    time.sleep(5)
    # open the text file
    file = open('NeverGonnaGiveUp.txt', 'r')
    # read the text file
    text = file.read()
    # close the text file
    file.close()
    # make a for loop that repeats the text file
    for i in range(100):
        # write the text file
        pyautogui.typewrite(text)
        # make a delay to make the spambot more realistic
        time.sleep(2.5)
        # make a new line
        pyautogui.press('enter')


# make it loop forever unless somone says to stop
while True:
    # make the spambot
    spamBot()
