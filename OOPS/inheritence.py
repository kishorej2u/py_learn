

class person:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    def printname(self):
        print(f"this is {self.name}from {self.city}")

p1 = person('kishore', 'chennai')
print(p1.printname())