import subprocess
import time
import pyautogui

source_input = input('Enter your Source: ')
destination_input = input('Enter your Destination: ')

def credentials_database():
    # Define the details you want to fill in
    global details
    details = {
        "indian_user": "test@indian",
        "american_user": "test@american",
        "british_user": "test@british",
        "australian_user": "test@australian",
        "russian_user": "test@russian"
    }
    
credentials_database()

def automate():
    # Define the path to the application you want to open
    app_path = "Terminal"
    # Open the application using subprocessb
    subprocess.Popen(["open", app_path])
    # Wait for the application to open
    time.sleep(1)  # Adjust the delay as per your application's launch time

def fill_credentials():
    # Define the coordinates of the input fields/buttons you want to interact with
    global field1_x,field1_y,field2_x,field2_y
    field1_x, field1_y = 100, 200
    field2_x, field2_y = 100, 250
    counter = 0
    for field, value in details.items():

        pyautogui.click(field1_x, field1_y)  # Click on the field
        pyautogui.typewrite('python3 Cooraj_CLI.py')  # Type the value
        pyautogui.press('return')
        time.sleep(1)
        
        pyautogui.click(field1_x, field1_y)  # Click on the field
        pyautogui.typewrite(field)  # Type the value
        pyautogui.press('return')
        #time.sleep(1)
        pyautogui.click(field2_x, field2_y)  # Click on the field
        pyautogui.typewrite(value)  # Type the value
        pyautogui.press('return')
        #time.sleep(1)
        pyautogui.click(field2_x, field2_y)  # Click on the field
        pyautogui.typewrite(source_input)  # Type the value
        pyautogui.press('return')
        #time.sleep(1)
        pyautogui.click(field2_x, field2_y)  # Click on the field
        pyautogui.typewrite(destination_input)  # Type the value
        pyautogui.press('return')



        #counter += 1

        #if counter == len(details):
            #break



# Define the path to the application you want to open
app_path = "Terminal"
# Open the application using subprocess
subprocess.Popen(["open", app_path])
# Wait for the application to open
#time.sleep(2)  # Adjust the delay as per your application's launch time

pyautogui.hotkey('command', 'n')
#time.sleep(1)
pyautogui.hotkey('command', 'n')
#time.sleep(1)


fill_credentials()



#wxpython
