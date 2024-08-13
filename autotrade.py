import pyautogui
import time
import csv
import os
import re

#Input the Absolute Path you have the CSV file
os.chdir(r'C:\Users\kangd\OneDrive\바탕 화면\Tonny\Projects\AutoTradeMacro')

def getAccounts(): 
    # List to store the second column's values
    accounts = []

    # Open the CSV file manually
    file = open('current.csv', mode='r', newline='')

    try:
        reader = csv.reader(file) 
        # Iterate over each row in the CSV file
        for row in reader:
            # Append the second column to the accounts list if it exists
            if len(row) > 1:
                accounts.append(row[2])
    
        
    finally:
        # Ensure the file is closed manually
        file.close()
    # Print the accounts list
    return accounts

def getPA():
    accounts=getAccounts()
    # Filter accounts to keep only those starting with "PA"
    filtered_accounts = [account for account in accounts if account.startswith("PA")]
    print("PA Accounts:",filtered_accounts)
    return filtered_accounts    

def sortPA():
    accounts=getPA()
    # Function to extract the number before '!Apex!Apex'
    def extract_number(account):
        match = re.search(r'(\d+)(?=!Apex!Apex)', account)
        if match:
            return int(match.group(1))  # Convert the matched number to integer
        return 0  # Default value if no number is found (though this shouldn't happen)
    # Sort the accounts based on the extracted number
    sorted_accounts = sorted(accounts, key=extract_number)

    # Print the sorted list
    print("Sorted accounts list:", sorted_accounts)

def csvExport(x, y):
    time.sleep(2)
    # Coordinates for the right click
    right_click_point = (x*0.136, y*0.192) # right click anywhere on the program

    # Coordinates for the left click
    left_click_point = (x*0.1635, y*0.340) # export

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

    left_click_point = (x*0.125, y*0.9200) #remote chrome keyboard input

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

    # We need to save in the same path as this script
    getAccounts()


x, y = pyautogui.size()

#csvExport(x, y)
sortPA()

