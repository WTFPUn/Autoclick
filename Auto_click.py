import pyautogui
import time

pyautogui.hotkey('alt', 'tab')
time.sleep(10)



pyautogui.mouseDown(button = 'left')
time.sleep(300)
pyautogui.mouseUp(button='left')
print('complete')


