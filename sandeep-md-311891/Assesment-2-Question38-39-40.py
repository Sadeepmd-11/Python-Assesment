#Question 38
class Pizza:
    def __init__(self, name,price):
        self.name=name
        self.price=price

    @classmethod
    def margherita(cls):
        return cls("margherita", 250)
    
    @staticmethod
    def validate_topping(toppingg):
        healthy=["tomato", "onion", "pineapple"]
        return toppingg.lower() in healthy
    
mypizza=Pizza.margherita()
valid=Pizza.validate_topping("pineapple")
print(f"pizza ordered={mypizza.name}")
print(f"is topping valid?={valid}")

#------------------------------------------------
#Question 39
class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)
    
p1=point(1,2)
p2=point(3,4)

print(p1+p2)

#---------------------------------------------------
#question40

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, length):
        self.length=length

    def area(self):
        return self.length * self.length
    
s=[Circle(5), Square(4)]
print(f"circle area: {s[0].area()}")
print(f"square area: {s[1].area()}")