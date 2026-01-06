n = int(input("Enter a number : "))

num = 1

for i in range(1,n+1):
    num = num * i
print(f"Factorial of {n} is {num}")