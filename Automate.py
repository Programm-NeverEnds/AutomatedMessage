import pyautogui   
import time


message="Em chestunavu??"


while True:
    time.sleep(3)
    pyautogui.typewrite(message)


    time.sleep(2)

    pyautogui.press('enter')


