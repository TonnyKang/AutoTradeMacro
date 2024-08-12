import pyautogui
import time

def csvExport(x, y):
    # Coordinates for the right click
    right_click_point = (x*0.136, y*0.192) # right click anywhere on the program

    # Coordinates for the left click
    left_click_point = (x*0.1635, y*0.3148) # export

    # Optional: Small delay to give you time before the script runs
    time.sleep(2)

    # Move the mouse to the right click point and perform a right-click
    pyautogui.moveTo(right_click_point)
    pyautogui.click(button='right')

    # Small delay between clicks
    time.sleep(0.5)

    # Move the mouse to the left click point and perform a left-click
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')

    left_click_point = (x*0.9541, y*0.9120) #remote chrome backspace to erase default name

    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')

    left_click_point = (x*0.125, y*0.9120) #remote chrome keyboard input

    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')

    time.sleep(0.1)
    # Type the new file name, "current"
    pyautogui.write("current")

    left_click_point = (x*0.9802, y*0.9120)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')

    # press two times more in case it asks to overwrite
    time.sleep(0.5)
    pyautogui.click(button='left')

    time.sleep(0.5)
    pyautogui.click(button='left')


x, y = pyautogui.size()

csvExport(x, y)

time.sleep(4)
pyautogui.moveTo((x*0.1896, y*0.2888))
pyautogui.click(button='right')

time.sleep(0.5)
pyautogui.moveTo((x*0.20, y*0.3101))
pyautogui.click(button='left')
