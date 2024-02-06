class Person:
    count = 0 # attribut de class
    def __init__(self, name):
        self.name = name # self.name est un attribut d'instance ou d'object
        Person.count += 1
    def greet(self): # method d'instance iu d'object
        pass

    @classmethod
    def amclassmethob(cls): # method de class
        return f"Hello I'm {cls.__name__}"

    @staticmethod
    def amstatic():
        return "I'm static"


person = Person("Fatima")
person2 = Person("Wass")

"""print(person.count)
print(person.name)
print(person2.name)
print(person2.count)
print(Person.count)
print(Person.name)
"""

"""print(type(Person.greet))
print(type(person.greet))"""

"""print(type(Person.amclassmethob))
print(Person.amclassmethob())
"""



print("###########héritage###########")



class Africain(Person):
    def __init__(self, name):
        super().__init__(name)


noir = Africain("Wassiou")
print(noir.amclassmethob())
