from random import randint 
n= randint(1,21)
while randint:
    if(n<19):
        print("go up", n)
        break
    elif(n>19):
        print("go down", n)
        break
    elif(n==19):
        print("win", n)
else:
    print("try again", n)
        