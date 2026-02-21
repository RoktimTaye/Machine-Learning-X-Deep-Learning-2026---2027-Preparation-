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
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dump(Bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        aplha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spachar = random.choices("!@#$%^&*",k = 1)
        id = aplha + num+ spachar
        random.shuffle(id)
        return "".join(id)
    
    def createaccount(self):
        info = {
            "name" : input("Tell your Name :- "),
            "age" : int(input("Tell your Age :- ")),
            "email" : input("Tell your Email :- "),
            "pin" : int(input("Tell your 4 digit pin :- ")),
            "accountNo" : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18 or len(str(info['pin'])) !=4:
            print("Sorry you cannot create your account")
        else:
            print("Account is created sucessfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your PIN number")
            
            Bank.data.append(info)
            Bank.__update()
    
    def depositmoney():
        pass
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

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()