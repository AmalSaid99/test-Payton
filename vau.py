v="aouei"
counter= 0
m=input("enter a text")
for chr1 in m:
    if(chr1.lower() in v):
        counter+=1
print(counter)