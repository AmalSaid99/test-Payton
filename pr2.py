ar1= input("enter elements of the first array: ")
ar2= input("enter elements of the second  array:  ")

for i in ar1:
    ar2.append(i)
    for x in ar2:
        print(ar2)
        if i>ar2[-1]:
            ar2.append(i)
        else:
            if (i<x):
                ar2.insert(ar2.index(x),(i))
                break
            print("the result: "+ar2)