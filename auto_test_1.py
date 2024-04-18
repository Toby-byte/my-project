import pyautogui
import time

time.sleep(2)

pyautogui.hotkey('ctrl', 'j')
pyautogui.hotkey('ctrl', 'j')

time.sleep(2)

pyautogui.hotkey('ctrl', 'shift', "'")

time.sleep(2)

pyautogui.write('.\Scripts\\activate')
pyautogui.press('enter')

time.sleep(2)

pyautogui.write('pip freeze > requirements.txt')
pyautogui.press('enter')

time.sleep(5)

pyautogui.write('pip install -r requirements.txt')
pyautogui.press('enter')

time.sleep(10)

pyautogui.write('deactivate')
pyautogui.press('enter')