class vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('details:',self.name,self.color,self.price)

    def max_speed(self):
        print("vechicle max speed is 150")       

    def change_gear(self):
        print('vehicle change 6 gear')


class car(vehicle):
    def max_speed(self):
        print('car max speed is 240')
    def change_gear(self): 
        print('car change 6 gear')            
car = car('car x1','red',200000)
car.show()
car.max_speed()
car.change_gear() 

#clauculte the area of different shapes. we'll create a base clas shape with an area()method ,and
# then create subclasses for specific shape like rectangle,circle,and triangle which will override the area
#()method to calculate the area specific to each shape


import math

class shape:
    def area(self):
        raise NotImplementedError("subclasses must implement this method")
    
class rectangle(shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height    


class circle(shape):
    def __init__(self,radius):
        self.radius = radius
        
class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base *self.height
    

#creating instance of diffferent shapes
rectangle = rectangle(5,4)
circle = circle(3)
triangle = triangle(6,8)   

print("area of rectangle:", rectangle.area())
print("area of circle:", circle.area())
print("area of triangle:", triangle.area())