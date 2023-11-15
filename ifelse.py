
g=input("enter your gender: ")

if (g.lower() =='m'):
     age= int(input("enter your age: "))
     if(24<=age<30):
       print("accepted")
     else:
       print("not accepted")

else:
    print("rejected")