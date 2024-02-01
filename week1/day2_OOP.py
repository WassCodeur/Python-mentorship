class Person:
    count = 0 # instant de class
    def __init__(self, name):
        self.name = name
        Person.count += 1

    def greet(self): # method (lorsqu'on l'appel avec un object
        print("Helle")


person1 = Person("Fatim")

#print(type(Person.greet)) function
#Person.greet()
print(type(person1.greet)) # method
person1.greet()


# https://www.pythontutorial.net/python-oop/?wt.mc_id=studentamb_232087
