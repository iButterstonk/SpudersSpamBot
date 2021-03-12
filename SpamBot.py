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
                            "Choice: "))
var = thing = 1


def spammer():




    
    time.sleep(2)

    if theChoice == 7:
        var = randNum = random.randrange(0, 4)
        var = fileName = open(fileArray[randNum], "r")
        print("the random generator picked ", randNum, " for you!")
        for word in fileName:
            pyautogui.typewrite(word)
            pyautogui.press("enter")




    else:
        var = fileName = open(fileArray[theChoice], "r")
        for word in fileName:
            pyautogui.typewrite(word)
            pyautogui.press("enter")


if thing == 1:
    madnessStopper = int(input("to stop the madness early type 2\n"
              "Type: "))
    madnessStopper = thing
    spammer()


