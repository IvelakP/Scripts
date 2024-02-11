import time
import pyautogui

def autoclicker(num_clicks):
    print("Autoclicker will start in 5 seconds...")
    time.sleep(5)
    
    print(f"Autoclicking {num_clicks} times...")
    for i in range(num_clicks):
        pyautogui.click()
    
    print("Autoclicking completed!")

# Get the number of clicks from the user
num_clicks = int(input("Enter the number of clicks: "))

# Start the autoclicker
autoclicker(num_clicks)