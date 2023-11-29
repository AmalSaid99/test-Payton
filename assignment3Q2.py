mylist = []
while len(mylist) < 10:
    num = int(input("enter 10 number: "))
    if num >= 1 and num <= 10:
        mylist.append(num)
        min_num= mylist[0]
for i in range(1, len(mylist)): 
    if (mylist[i] < min_num):
        min_num = mylist[i]
print(mylist)
print(mylist.index(min_num))
        
