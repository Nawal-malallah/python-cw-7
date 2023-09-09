

class Person:
   
    def __init__(self, name, age, list):
        self.name = name 
        self.age = age
        self.hobbies = list 
    
firstPerson = Person("m", 2, [1,3,3])
print(firstPerson.hobbies)



class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
      return f"My name is {self.name} and I am {self.age} years old "  

    def isAdult(self):
        if self.age >= 18:
            return "You have too much responsibilities"
        else:
            return "Lucky you"

firstPerson = Person("me", 3 )
print(firstPerson.name)
print(firstPerson.age)
print(firstPerson.isAdult())
print(firstPerson)
