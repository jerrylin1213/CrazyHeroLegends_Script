from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import array
from datetime import datetime

# Positions of Buttons
TITLEBAR_HEIGHT = 30
GAME_RATIO = 0.56
GAME_HEIGHT = pyautogui.size()[1] - TITLEBAR_HEIGHT
GAME_WIDTH = round(GAME_HEIGHT * GAME_RATIO)
WINDOW_SIZE = (GAME_WIDTH, GAME_HEIGHT)

start_gambling_pos = (GAME_WIDTH * 0.5, GAME_HEIGHT * 0.6 + 30)
ten_K_chips_pos = (GAME_WIDTH * 0.8, GAME_HEIGHT * 0.82 + 30)
one_K_chips_pos = (GAME_WIDTH * 0.18, GAME_HEIGHT * 0.79 + 30)
# small_pos = (GAME_WIDTH * 0.78, GAME_HEIGHT * 0.57 + 30)
small_pos = (GAME_WIDTH * 0.22, GAME_HEIGHT * 0.57 + 30)
add_chip_pos = (GAME_WIDTH * 0.5, GAME_HEIGHT * 0.78 + 30)
close_window = start_gambling_pos
message_box = (GAME_WIDTH * 0.4, GAME_HEIGHT * 0.4 + 30, GAME_WIDTH * 0.6, GAME_HEIGHT * 0.44 + 30)
# win_color = 33625
win_color = GAME_HEIGHT * 30
num_of_iteration = ""


def if_lost():
    img = ImageGrab.grab(message_box)
    image = ImageOps.grayscale(img)
    a = array(image.getcolors())
    return a.sum() > win_color

def start_gambling():
    pyautogui.click(start_gambling_pos)
    time.sleep(0.1)
    pyautogui.click(ten_K_chips_pos)
    for i in range(8):
        pyautogui.click(add_chip_pos)
        time.sleep(0.05)
    pyautogui.click(small_pos)

def make_up_round():
    pyautogui.click(start_gambling_pos)
    time.sleep(0.1)
    pyautogui.click(one_K_chips_pos)
    for i in range(6):
        pyautogui.click(add_chip_pos)
        time.sleep(0.05)
    pyautogui.click(small_pos)


# main
count = win = lose = earned= 0
start_time = datetime.now()

try:
    while not num_of_iteration.isdigit():
        num_of_iteration = input("How many rounds do you want to run? ")
    for i in range(int(num_of_iteration)):
        start_gambling()
        time.sleep(7)
        if if_lost():
            pyautogui.click(close_window)
            make_up_round()
            lose += 1
        else:
            pyautogui.click(close_window)
            count += 1
        print(f"Total game: {count}; Lose: {lose}")
except:
    stop_time = datetime.now()

    print("Total Time = ", stop_time-start_time)
    print(f"You've earn: {(count-lose) * 90000 - lose * 20000}")
