class circle ():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*circle.pi

    def set_radius(self, new_r):
        self.radius = new_r    
mycircle = circle()
mycircle.set_radius = 500
print (mycircle.area())


