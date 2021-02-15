import pyautogui
import time

time.sleep(10)

file = "filename.txt"
wait_val = 3
f = open(f"{file}", "r")
for word in f:
    time.sleep(1)
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(wait_val)
