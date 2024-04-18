import time
import pyautogui
import pyperclip
import os
import subprocess

os.startfile('chrome.exe')

time.sleep(2)

pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://github.com/arturomorarioja?tab=repositories&q=&type=&language=&sort=')
time.sleep(2)
pyautogui.press('enter')

pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://kea-fronter.itslearning.com/index.aspx?SessionExpired=0')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press("tab")
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')

base_path = "C:\\Users\\Lenovo\\OneDrive IT Center Fyn\\Skrivebord\\1. sem Repo's\\User_experience\\Web24v_Webshop"

# Full path to VSCode's executable
# Formattet i path skal være præcis som vist ellers virker det ikke
vscode_executable_path = 'C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'

# Path to the directory you want to open
directory_path = f'{base_path}'

# Open the directory in VSCode using the full path to the executable
subprocess.run([vscode_executable_path, directory_path])