#! python3
# spiralDraw.py - Draw using mouse

import pyautogui, time

# Pause for 10 seconds to allow you move to MS paint
# And select the brush
time.sleep(10)

pyautogui.click() # click to put drawing program in focus
# set size
distance = 400
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2) # move down
    pyautogui.dragRel(-distance, 0, duration=0.2) # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2) # move up
