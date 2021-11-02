a = input("Enter Words : ").split(" ")
b = set(a)
b = list(b)
b.sort()
for i in b:
    print(i, end=" ")
