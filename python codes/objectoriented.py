class dog ():
    # class object attributes
    species  ="mammel"
    def __init__(self,breed, name):
        self.breed = breed
        self.name = name

mydog = dog("labra", "jojo")
print (mydog.breed)
print (mydog.name)
print (mydog.species)