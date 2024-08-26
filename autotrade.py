import pyautogui
import time
import csv
import os
import re
from collections import deque

#Input the Absolute Path you have the CSV file
# os.chdir(r'C:\Users\kangd\OneDrive\바탕 화면\Tonny\Projects\AutoTradeMacro')

# Gets all accounts available
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

# Filters out PAs from all accounts
def getPA():
    accounts=getAccounts()

    # Calculate the total number of accounts
    total = len(accounts) - 1

    # Filter accounts to keep only those starting with "PA"
    # filtered_accounts = [account for account in accounts if account.startswith("PA")]
    filtered_accounts = [account for account in accounts if account.startswith("APEX")]
    print("PA Accounts:",filtered_accounts)

    return filtered_accounts, total

# Returns the PAs that we want
def transactionPA():
    accounts, total = getPA()

    # Calculate the length of the filtered accounts list
    filtered_len = len(accounts)

    # Input the today's accounts number from user
    today_accounts = list(map(int, input("오늘 거래할 계좌의 숫자를 입력해주세요 : ").split(',')))

    # Function to extract the number before '!Apex!Apex'
    def extract_number(account):
        match = re.search(r'(\d+)(?=!Apex!Apex)', account)
        if match:
            return int(match.group(1))  # Convert the matched number to integer
        return 0  # Default value if no number is found (though this shouldn't happen)
    
    # Sort the accounts based on the extracted number
    sorted_accounts = sorted(accounts, key=extract_number)

    # Find the index of today's accounts in the sorted list and create a new list with the result
    accounts_to_use = deque()

    for idx, account in enumerate(sorted_accounts):
        if extract_number(account) in today_accounts:
            accounts_to_use.append((account, idx))

    return accounts_to_use

# Exports the current cells into a CSV file
def csvExport():
    global x,y
    time.sleep(2)
    # Coordinates for the right click
    right_click_point = (x*0.1786, y*0.1935) # right click anywhere on the program

    # Coordinates for the left click
    left_click_point = (x*0.2052, y*0.3342) # export

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

    #left_click_point = (x*0.9536, y*0.9166) #remote chrome backspace to erase default name
    # Press the Backspace key
    pyautogui.press('backspace')
    #pyautogui.moveTo(left_click_point)
    #pyautogui.click(button='left')

    #left_click_point = (x*0.125, y*0.9166) #remote chrome keyboard input
    
    #pyautogui.moveTo(left_click_point)
    #pyautogui.click(button='left')

    time.sleep(0.1)
    # Type the new file name, "current"
    pyautogui.write("current")

    left_click_point = (x*0.9869, y*0.9166)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')

    # press two times more in case it asks to overwrite
    time.sleep(0.5)
    pyautogui.click(button='left')

    time.sleep(0.5)
    pyautogui.click(button='left')

    # We need to save in the same path as this script

# Sets the accounts we want to use to the domes, the accounts list should have only 3
def selectAccount(accounts):
    dy = y*0.0170
    # 각 dom Account 좌표
    for x, y in [(x*0.6989, y*0.3379), (x*0.6989, y*0.5861), (x*0.6989, y*0.8129)]:
        if accounts:
            _, d = accounts.popleft()
        else:
            break
        
        #pyautogui.click(x, y)
        #time.sleep(0.5)
        pyautogui.keyDown('up') # up 키를 누른 상태를 유지합니다.
        time.sleep(1)
        pyautogui.keyUp('up') # up 키를 뗍니다.

        pyautogui.press('down', presses=d, interval=0.1) #  down 키를 0.1초에 한번씩 d번 입력합니다. 
        pyautogui.press('enter')

        #y += dy*(d+1)
        #pyautogui.click(x, y)

def setInstrument():
    # > 첫번째 슈퍼돔은 NQ 09-24
    left_click_point = (x*, y*)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')
    pyautogui.write("NQ 09-24")

    # > 두번째 슈퍼돔은 YM 09-24
    left_click_point = (x*, y*)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')
    pyautogui.write("YM 09-24")

    # > 세번째 슈퍼돔은 GC 08-24
    left_click_point = (x*, y*)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')
    pyautogui.write("GC 08-24")

    return True

# input which dome to set, if 0, set all of them
def setQuantity(i):
    # >첫번째 슈퍼돔은 1, 2 고정
    # > 두번째 슈퍼돔은 2, 4 고정
    # > 세번째 슈퍼돔은 1, 2 고정
    if not i:
        left_click_point = (x*, y*)
        pyautogui.moveTo(left_click_point)
        pyautogui.click(button='left')
        pyautogui.press('backspace')
        pyautogui.write('1')

        left_click_point = (x*, y*)
        pyautogui.moveTo(left_click_point)
        pyautogui.click(button='left')
        pyautogui.press('backspace')
        pyautogui.write('2')

        left_click_point = (x*, y*)
        pyautogui.moveTo(left_click_point)
        pyautogui.click(button='left')
        pyautogui.press('backspace')
        pyautogui.write('1')
    else:
        # initialize the ith dome

    return True


def setATMStrat():
    # > 첫번째 슈퍼돔은 1로 고정
    left_click_point = (x*, y*)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')
    left_click_point = (x*, y*)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')

    # > 두번째 슈퍼돔은 2로 고정
    left_click_point = (x*, y*)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')
    left_click_point = (x*, y*)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')

    # > 세번째 슈퍼돔은 3로 고정
    left_click_point = (x*, y*)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')
    left_click_point = (x*, y*)
    pyautogui.moveTo(left_click_point)
    pyautogui.click(button='left')

    # > Account가 변경될때 이게 none 으로 변경될수도 있어서
    # Account가 변경되거나 거래가 마무리되면 확인해야함

    return True

# Returns 3 GrossReals, Ideally for the accounts we are trading with
def getGrossReal(i,j,k):
        # List to store 
    gross_real = []

    # Open the CSV file manually
    file = open('current.csv', mode='r', newline='')

    try:
        reader = csv.reader(file) 
        # Iterate over each row in the CSV file
        for row in reader:
            # Append the 10th column to the gross_real list if it exists
            if len(row) > 1:
                gross_real.append(row[10])
    
        
    finally:
        # Ensure the file is closed manually
        file.close()
   
    return gross_real[i], gross_real[j],gross_real[k]

# Doubles Quantity if GrossReal is Negative
# for the ith dome
def doubleQuantity(i):
    
    return True

# The transaction that will go on
def transaction():
    # Get the Accounts we are going to use
    accounts=transactionPA()
    # Initial Instruments
    setInstrument()
    setQuantity()
    setATMStrat()   

    domeStatus=[] # Holds the current accounts in domes

    # 3 Domes
    domeStatus.append(accounts.pop(0))
    domeStatus.append(accounts.pop(0))
    domeStatus.append(accounts.pop(0))

    # The First 3 Accounts
    selectAccounts(domeStatus)
    
    while(1):
        #
        #
        #
        #ACTUAL TRANSACTION CODE NEEDED HERE
        #
        #
        #
        current_gross_real=getGrossReal(domeStatus[0][1],domeStatus[1][1],domeStatus[2][1])

        for i in range(3):
            # If GrossReal is Green
            if current_gross_real[i]>0:
                if accounts: 
                    domeStatus[i]=accounts.pop(0)
                # No more accounts
                else:
                    domeStatus[i]=(0,0)
            # If GrossReal is Red
            else:
                doubleQuantity(domeStatus[i][0])
        
        if  domeStatus[0][0]==0 and domeStatus[1][0]==0 and domeStatus[2][0]==0:
            # We've done al the accounts
            break
        else:
            # Set the new accounts and go again
            selecttAccounts(domeStatus)

                
                


          


# Main Function
def main():
    x, y = pyautogui.size()

    # csvExport()
    accounts=transactionPA()

    print(accounts)

    selectAccount(x, y, accounts)

if __name__ == "__main__":
    main()