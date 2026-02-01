l = list(map(int,input("Enter the numbers :- ").split()))

largest = l[0]
Sec_largest = l[0]

for i in range(len(l)):
    if largest < l[i]:
        Sec_largest = largest
        largest = l[i]
    elif Sec_largest < l[i]:
        Sec_largest = l[i]
print(f"Largest Number is {largest}")
print(f"Second Largest Number is {Sec_largest}")