

# class Arha:
#     Age = 2.4

# obn = Arha()
# print(obn.Age)




# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print('this is ' + (self.name))
        
        
# p1 = person("arha", 2)
# print(p1.age)
# print(p1.name)

# p1.greet



# class Person:
#   def __init__(myobject, name, age):
#     myobject.name = name
#     myobject.age = age

#   def greet(abc):
#     print("Hello, my name is " + abc.name)

# p1 = Person("Emil", 36)
# p1.greet()





# class car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def makeyear(self):
#         return (f"{self.year} and {self.brand} and {self.model}")

#     def facelift(self):
#         mes = self.makeyear()
#         print(mes , 'this is the facelift message')


# a = car('tata', 'punch', '2026')
# # a.makeyear()
# a.facelift()
# a.model = 'nexon'
# a.facelift()
# print(a)
# del a.model
# print(a.model)
# del a
# print(a)





# class person:
#     nam = ''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def ega(self):
#         self.age += 1
#         return self.age


# p1 = person('kishore', 31)
# print(p1.name)
# print(p1.nam)
# person.nam = 'arha'
# print(p1.nam)
# p1.city = "chennai"
# print(p1.city)
# print(p1.ega())
# print(p1.ega())



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Emil", 36)
print(p1)