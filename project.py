class Circle:
    def __init__(self,r):
        self.radius=r

    def area(self):
        return self.radius**2*3.1416
    
    def parameter(self):
        return 2*self.radius*3.14

    
radius=int(input("Please enter the radius:"))
circle2=Circle(radius)
print(circle2.area())
print(circle2.parameter())