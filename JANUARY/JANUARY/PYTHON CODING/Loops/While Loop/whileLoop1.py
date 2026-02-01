n = int(input("Enter the number to seperate the digits and print on new line : "))

while n>0:
    digit = n % 10
    print(digit)
    n = n // 10