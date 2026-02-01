l = [23,24,28,29]

for i in range(len(l)-1):
    if l[i] <= l[i+1]:
        continue
    else:
        print("List is not sorted")
        break
else:
    print("List is Sorted")
