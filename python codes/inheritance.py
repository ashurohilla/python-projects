class Animal ():
    def __init__(self):
        print ("animal created")
         
    def whoami(self):
        print ("animal")
    def eat(self):
        print ('eating')
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("dog created using base class")
    def bark(self):
        print("whoof")            


mydog = Dog()
mydog.whoami()
mydog.eat()
mydog.bark()
 
                 