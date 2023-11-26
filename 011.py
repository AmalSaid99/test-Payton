size= int(input("enter a number: "))
for i in range(size):
    for j in range(size):
        if (i<=j):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
