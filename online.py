import pyautogui
import random
import time

while True:
    # Get the screen size
    screenWidth, screenHeight = pyautogui.size()
    
    # Generate random coordinates within the screen size
    x = random.randint(0, screenWidth)
    y = random.randint(0, screenHeight)
    
    # Move the mouse to the random coordinates
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 1))
    
    # Pause for a random amount of time
    time.sleep(random.uniform(0.5, 2))
