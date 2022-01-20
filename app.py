from PIL import ImageGrab
from PIL import ImageOps
from pip import main
import pyautogui
import time
from numpy import *
from datetime import datetime

winColor = 35000
small = (1700, 700)
start = (1630, 700)
ten_thousand = (1750, 980)
thousand = (1340, 930)
more = (1550, 930)
winBoxStart = (1490, 490)
winBoxEnd = (1630, 540)
closeWindow = (1550, 710)


def startGambling():
    pyautogui.click(start)
    time.sleep(0.05)
    pyautogui.click(ten_thousand)
    for i in range(8):
        pyautogui.click(more)
        time.sleep(0.05)
    pyautogui.click(small)

def winOrLose():
    winWord = (winBoxStart[0], winBoxStart[1], winBoxEnd[0], winBoxEnd[1])
    winImage = ImageGrab.grab(winWord)
    grayImage = ImageOps.grayscale(winImage)
    a = array(grayImage.getcolors())
    return a.sum()

def ifLose():
    pyautogui.click(closeWindow)
    time.sleep(0.05)
    pyautogui.click(start)
    time.sleep(0.05)
    pyautogui.click(thousand)
    for i in range(6):
        pyautogui.click(more)
        time.sleep(0.05)
    pyautogui.click(small)

# main
COUNT = 0
LOSE = 0
time.sleep(2)
NOW = datetime.now()
try:
    while COUNT < 1000:
        time.sleep(0.5)
        startGambling()
        time.sleep(7.5)
        if winOrLose() > winColor:
            ifLose()
            LOSE+=1
        else:
            pyautogui.click(closeWindow)
            COUNT+=1
        print(f"Total game: {COUNT}; Lose: {LOSE}")
except:
    STOP = datetime.now()

    totalTime = (STOP-NOW)

    print("Total Time = ", totalTime)
    print(f"You've earn: {(COUNT-LOSE) * 90000 - LOSE * 20000}")
