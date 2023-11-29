class Person:
    def __init__(self, name, age):
        self.name=  name 
        self.age = age
    def __str__(self):
        return"hello {} you are {} years old".format(self.name,  self.age)
person1 = Person("Amal", 24)
print(id(person1))
print(type(person1))
print(person1)