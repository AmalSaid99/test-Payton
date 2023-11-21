s= "abc"
list_= s.split("b")
print(list_)

#copy in each list
print("**********")
s= [2,5,5,1,7]
x= s
x[4]= 5
print(s)
s[3]= 77
print(x)

#one list change 
print("**********")
s= [2,5,5,1,7]
x= s.copy()
x[4]= 5
print(s)
s[3]= 77
print(x)

#
print("**********")
x= [1,2,3]
s=list(x)
print(x[-1])