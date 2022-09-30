import pyautogui   
import time


message="What's Up!"


while True:
    time.sleep(2)
    pyautogui.typewrite(message)


    time.sleep(2)

    pyautogui.press('enter')


