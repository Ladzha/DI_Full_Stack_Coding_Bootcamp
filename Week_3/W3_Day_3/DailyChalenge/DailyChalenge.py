class Circle:
    
    def __init__(self, diameter=0, radius=0):
        self.radius=float(radius)
        self.diameter=float(diameter)
        # self.area=float(area)   
        all_circle = []
        
    def __add__(self, other_circle):
        self.circe_area = other_circle.circe_area
        
    def __gt__(self, other_circle):
        if self.circe_area > other_circle.circe_area:
            return self.circe_area
        else:
            other_circle.circe_area
    
    def add_circle(self, other_circle):
        self.all_circle.append(other_circle)
        print(self.all_circle)

    @classmethod   
    def get_radius(cls, diameter):
        return cls(diameter=diameter,radius=diameter/2)
    
    @classmethod   
    def get_diameter(cls, radius):
        return cls(radius=radius, diameter=radius*2)
    
    def get_area(self):
        self.area = 3.14*2*self.radius*2
        return self.area

circleA = Circle.get_radius(diameter=4)
circleB = Circle.get_diameter(radius=4)
circleA.get_radius(4)
circleA.get_diameter(6)

# print(circleA > circleB)

print(circleA.radius)
print(circleA.diameter)
print(circleA.get_area())




