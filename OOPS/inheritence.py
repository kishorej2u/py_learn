

class person:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    def printname(self):
        print(f"this is {self.name}from {self.city}")

# p1 = person('kishore', 'chennai')
# print(p1.printname())

class child(person):
    def __init__(self, name, city, year):
        super().__init__(name, city)
        # self.name = name
        # self.city = city
        self.grad = year
    
    def hello(self):
        print(f'this is {self.name}')
    # pass
    def printname(self):
        print(f"this is {self.name}from {self.city} from child")
    

p2 = child('arha', 'chennai', 2034)
# print(p2.printname())
print(p2.printname())
print(p2.grad)
p2.hello()