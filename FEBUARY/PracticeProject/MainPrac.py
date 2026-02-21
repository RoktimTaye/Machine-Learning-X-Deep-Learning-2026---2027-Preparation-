import random
import json
import string
from pathlib import Path
class Bank:
    database = 'data,json'
    data = []
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        aplha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("@#$%^&*",k = 1)
        id = aplha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createaccount():
        info = {
            "name" : input("Tell your Name :- "),
            "age" : int(input("Tell your age :- ")),
            "email" : input("Tell your email :-"),
            "pin" : int(input("Tell your 4 digit pin :- ")),
            "accountNo" : Bank.__accountgenerate(),
            "balance" : 0
        }
user = Bank()
print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :- "))

if check == 1:
    user.Createaccount()

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