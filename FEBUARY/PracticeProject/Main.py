import json
import random
import string
from pathlib import Path
class Bank:
    database = 'data.json'
    data = []
    # Data Loading is Performed With Incase Exception Handling
    try:    
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs.read())
        else:
            print("No Such File Exists")
    except Exception as err:
        print(f"An Exception has occured as {err}")
        
    def createaccount(self):
        info = {
            "name" : input("Tell your Name :- "),
            "age" : int(input("Tell your Age :- ")),
            "email" : input("Tell your Email :- "),
            "pin" : int(input("Tell your 4 digit pin :- ")),
            "accountNo" : 1234
        }
        if info['age'] < 18 or len(str(info['pin'])) !=4:
            print("Sorry you cannot create your account")
        else:
            print("Account is created sucessfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your PIN number")
            
            Bank.data.append(info)
        
user = Bank()
print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("Tell your response :- "))

if check == 1:
    user.createaccount()