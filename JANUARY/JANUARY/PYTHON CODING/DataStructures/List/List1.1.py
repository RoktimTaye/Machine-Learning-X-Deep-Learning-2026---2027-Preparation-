l = list(map(int, input("Enter the numbers :- ").split()))

print("------Positive Numbers------")
for i in range(len(l)):
    if l[i] > 0 :
        print(l[i])

print("------Negative Numbers------")
for i in range(len(l)):
    if l[i] < 0 :
        print(l[i])