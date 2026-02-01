l = list(map(int,input("Enter the numbers to find Mean :- ").split()))

sum  = 0

for i in range(len(l)):
    sum += l[i]
    length = len(l)
    mean = sum / length

print(f"Mean of the numbers is {mean}")