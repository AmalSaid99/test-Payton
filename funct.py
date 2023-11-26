def read_float(n):
    num1=[]
    for i in range(n):
        num= float(input("enter a number: "))
        num1.append(num)
    return(num1)

def mul_func(list1, factor):
    for i in range (len(list1)):
        list1[i]= list1[i]*factor
    return list1

def reverse_func(list1):
    list1.reverse()
    return list1

def main():
    my_list= read_float(3)
    number= int(input("enter the factor: "))
    new_list= mul_func(my_list, number)
    result= reverse_func(new_list)
    print(result)
main()
    
    
    