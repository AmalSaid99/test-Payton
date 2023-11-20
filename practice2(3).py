sum1= 0
for num in range (1,101):
    for i in range(1, num):
        if(num%i==0):
            sum1+=i
             
    if(sum1==num):
        print(num)
    sum1=0
