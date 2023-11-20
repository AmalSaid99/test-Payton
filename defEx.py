def main():
    print(func1(2),func2(1))
def func1(x):
    num = 5
    return x*num
def func2(x):
    i=2
    y=3
    return i*x+y
main()



############
def sum_digits(x):
    
    sum1=0
    while(x!=0):
        sum1+=x%10
        x=x//10
    print(sum1)
        
        
sum_digits(234)

# ###############
sum1 = 0
result= 0
n=int(input("enter the number: "))
for i in range(1, n+1):
   result= "2"*i
   sum1 +=int(result)
   print(result)
print(sum1)
        
