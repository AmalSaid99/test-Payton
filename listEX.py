#space between numbers
s= [2,5,5,1,7]
for i in s:
    print(i, end=" ")
    
print("**********")
#each number multiple 2
s= [2,5,5,1,7]
for i in s:
    i=i*2
    print(i, end=" ")

print("**********")
#negetive number
s= [-2,5,5,1,-7]
count=0
for i in s:
    if(i<0):
        count+=1
print(count)