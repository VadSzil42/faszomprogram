class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printInfo(self):
        print(self.name + ' vagyok es ' + str(self.age))

person1 = Person("Joshua", 12)
person2 = Person("Mateo", 15)
person3 = Person("Albert", 14)

person1.printInfo()