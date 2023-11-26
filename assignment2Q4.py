fruits= ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
a=fruits.count("apple")
print(a)
b=fruits.count("strawberry")
print(b)
c=fruits.index("banana")
print(c)

d=fruits.index("banana", 4)
print(d)

fruits.reverse()
print(fruits)

fruits.append("grape")
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)
