import pyautogui
import win32gui

# First, we need to find the window we want to move.
# We can use its title name as an identifier.
title = "Notepad"
hwnd = win32gui.FindWindow(None, title)
if hwnd == 0:
    print(f"Could not find window '{title}'.")
    exit()

# Next, we'll get the current position of the window.
# This will be our starting point for the movement.
prev_pos = win32gui.GetWindowRect(hwnd)
x0, y0, x1, y1 = prev_pos

# We'll set a new position for the window, by adding a
# horizontal offset of 100 pixels and a vertical offset
# of 50 pixels to its previous position.
dx, dy = (100, 50)
new_pos = (x0+dx, y0+dy, x1+dx, y1+dy)

# Now, we'll move the window by simulating a left-mouse-button
# click-and-drag action at its previous and new positions.
pyautogui.mouseDown(x=x0, y=y0, button='left')
pyautogui.moveTo(x=new_pos[0], y=new_pos[1], duration=1)
pyautogui.mouseUp(x=new_pos[0], y=new_pos[1], button='left')

# Finally, we'll check that the window has indeed moved
# to its new position by getting its updated coordinates.
curr_pos = win32gui.GetWindowRect(hwnd)
if curr_pos == new_pos:
    print(f"Window '{title}' moved successfully.")
else:
    print(f"Window '{title}' failed to move.")
