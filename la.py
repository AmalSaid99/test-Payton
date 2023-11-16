n=int(input("enter no: "))
while n in range(1,21):
    if(n<19):
        print("go up")
        break
    elif(n>19):
        print("go down")
        break
    elif(n==19):
        print("win")
else:
    print("try again")
        
    
        