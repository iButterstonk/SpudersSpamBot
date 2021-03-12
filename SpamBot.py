import pyautogui
import time
import random

let = fileArray = ["BeeMovie",
                   "NeverGonnaGiveUp",
                   "randomgiberish",
                   "FORTNITE",
                   "howboutno",
                   "Hello"]
let = theChoice = int(input("What do you want to spam with \n"
                            "0.Bee Movie Script\n"
                            "1.Never Gonna Give you up lyrics\n"
                            "2.Random Gibberish\n"
                            "3.Fortnite spamming\n"
                            "4.The words How About No\n"
                            "5.Spam Hello\n"
                            "6.idk pick something random\n"
                            "7.Counting\n"
                            "Choice: "))
var = thing = 1


def spammer():
    time.sleep(2)
    if theChoice == 6:
        var = randNum = random.randrange(0, 5)
        var = fileName = open(fileArray[randNum], "r")
        print("the random generator picked ", randNum, " for you!")
        for word in fileName:
            pyautogui.typewrite(word)
            pyautogui.press("enter")

    if theChoice == 7:
        let = start = int(input("What number do you want to start at"
                                "Start: "))
        let = numbers = open("Numbers", "r")
        for word in numbers:
            time.sleep(0.02)# pretty useless but it will be use full soon :)
            let = addedNums = start + 1
            pyautogui.typewrite(str(addedNums))
            pyautogui.press("enter")
            start = addedNums




    else:
        var = fileName = open(fileArray[theChoice], "r")
        for word in fileName:
            pyautogui.typewrite(word)
            pyautogui.press("enter")


if thing == 1:
    spammer()
