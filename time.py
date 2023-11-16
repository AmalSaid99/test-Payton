hour1= int(input("enter a hour for first time: "))
minit1= int(input("enter a min for first time: "))
APm1= int(input("enter a am or pm for first time: "))

hour2=int(input("enter a hour for second time: "))
minit2=int(input("enter a min for second time: "))
APm2= int(input("enter a am or pm for second time: "))

if(APm1 == "am" and APm2 == "pm"):
    print("first time is first: "+ str(hour1)+":"+str(minit1)+APm1)
elif(APm1 == "am" and APm2 == "pm"):
        print("second time is first: "+ str(hour2)+":"+str(minit2)+APm2)
else:
            
            if(h1 <h2):
                print("first time is first "+str(hour1)+":"+str(minit1)+APm1)
            elif(hour1 == hour2):
                 if(minit1<=minit2):
                    print("first time is fist "+ str(hour1)+":"+str(minit1)+APm1)
                else:
                        print("second time is fist "+ str(hour2)+":"+str(minit2)+APm2)
            else:
             print("second time is first "+str(hour2)+":"str(minit2)+APm2)






