
dic= {1:"A", 2:"B"}
print(dic.get(5,"s"))

#delete specific key and value
dic= {1:"A", 2:"B"}
print(dic.pop(2))
print(dic)
#print only values
dic= {1:"A", 2:"B"}
for x in dic:
    print(dic[x])
#print only key  
dic= {1:"A", 2:"B"}
for x in dic:
    print(x)
#print key and value in ()
dic= {1:"A", 2:"B"}
for x in dic.items():
    print(x)