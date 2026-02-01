n = input("Enter the String to check if its palindrome or not : ")

b = ""

for i in range(len(n)-1,-1,-1):
    b+= n[i] 

if b == n:
    print("Thee string is Palindrome")
else:
    print("Thee string is not Palindrome")