balance=100
PIN= int(input("enter your PIN: "))
if(PIN==1234):
    
    no=int(input("enter no: "))
    if(no==1):
        print("your balance", balance)
        
    elif(no==2):
        cost= float(input("How much you want?" ))
        ag=(balance-cost)
        print(ag)
        
    elif(no==3):
        amount= float(input("How much you want to add?" ))
        ag2=(amount+balance)
        print("your balance now is: " ,ag2)
    else:
        print("try again")
        
else:
    print("sorry, try again")
        
        
    
    
    
    