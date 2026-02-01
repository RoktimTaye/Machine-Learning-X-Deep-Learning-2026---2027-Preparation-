import random

num = random.randint(1,50)

tries = 0
# print(num)
while True:
    guess = int(input("Enter the guessed number : "))
    
    if guess == num:
        tries+=1
        print(f"You Guessed the correct number in {tries} tries")
        break
    elif guess > num:
        tries+=1
        print("Go little down")
    elif guess < num:
        tries+=1
        print("Go little higher")
    else:
        tries+=1
        print("You Guessed the worng Number")