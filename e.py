class Person:
         def _init_(self, name, age=22): 
                self.__name=  name 
                self.__age = age
         def say_hi(self):
            print("hello {} from parent class".format(self.name))
class Student(Person):
         def _init_(self, name, age=22):
             super()._init_(name,age)
         def say_hi(self):
             print("hello {} from student class".format(self.name))
p1=Person("A", 22)
s1= Student("B", 15)
s1.say_hi()
p1.say_hi()