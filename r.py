class Person:
        num_of_object=0
     def __init__(self, name, age=22): 
            self.__name=  name 
            self.__age = age
            Person.num_of_object +=1
     def set_name(self, new_name):
        self.__name = new_name
        
     def get_name(self):
        print(self.__name)
     def __str__(self):
        return"hello {} you are {} years old".format(self.name,self.age)
     def talk(self):
        return "{} is talking".format(self.name)
person1 = Person("Amal", 24)
person2= Person("bbbb", 24)
print(person2.__str__())
print(person1)

