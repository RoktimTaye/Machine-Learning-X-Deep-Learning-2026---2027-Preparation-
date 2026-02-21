import random 
import json
import string
from pathlib import Path

class Bank:
    def createaccount():
        info = {
            'name' : input('Tell your name :- '),
            'age' : int(input('Tell your age :- ')),
            'email' : input('Tell your email :- '),
            'pin' : int(input('Tell your 4 digit pin number :- ')),
            'accountNo' : 1234,
            'balance' : 0
        }
# user = Bank()

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