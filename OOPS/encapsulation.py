

class house:
    def __init__(self,name, age):
        self.name = name
        self.__age = age

    def ret(self):
        return self.__age
    
    def __prot(self):
        return self.name
    
    def ret2(self):
        return self.__prot()

p1 = house('kishore', 31)
print(p1.name)
#print(p1.age)
print(p1.ret())
print(p1.ret2())