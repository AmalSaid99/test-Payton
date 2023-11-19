numb= int(input("enter number: "))
def check_type(number):
    if(number%2 ==0):
       return "even number"
    else:
        return "odd number"
n= check_type(numb)
print(n)


