i = 0
n = int(input("no: "))
s=0
while(i<len(str(n))):
      s+=n%10
      n=n//10
      i+=1
print(s)