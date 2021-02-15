import pyautogui
import time

time.sleep(10)

run = 1
amount_of_repetitions = 10
wait_val = 3

while run < amount_of_repetitions:
    pyautogui.typewrite('<text>')
    time.sleep(wait_val)
    pyautogui.press('enter')
    run = run + 1
