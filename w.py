class sh:
    def __init__(self, col, nam): 
            self.col=  col 
            self.nam = nam
            self.discr = discr
class sq(sh):
    def __init__(self, col, nam, area, discr):
        super()._init_(col, nam)
        #def area(self, l):
            #return "hello {} you are {} years old".format(self.name,self.age)
class cy(sh):
    def __init__(self, col, nam, area, discr):
        super()._init_(col, nam)
        def area(self, r):
            ar=area*3.14
            return "the area of cr is: ".format(self.col,self.nam,self.area,self.discr)
    def __str__(self):
        return"are".format(self.col,self.nam)
sq1= sh("blue","hhh",7 )
cy1= sh("red","cccc",9 )
print(sq1.__str__())
print(sq1)
print(cy1)


