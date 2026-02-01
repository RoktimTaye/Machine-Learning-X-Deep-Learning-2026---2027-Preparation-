n = int(input("Enter the number : "))

copy = n
rev = 0

while n > 0 :
    rev = rev * 10 + n % 10
    n = n // 10

if copy == rev:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")