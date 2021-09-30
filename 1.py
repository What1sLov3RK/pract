# 1. Create a class Rectangle with attributes length and width, each of which defaults to 1. Provide methods that calculate the perimeter and the area of the rectangle.
# Also, provide setter and getter for the length and width attributes. The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0.
class Rectangle(object):
    def __init__(self,length=1,width=1):
        self.length=length
        self.width=width
        if length>0 and length< 20:
            pass
        else :
            self.length=1
        if width > 0 and width < 20:
            pass
        else:
            self.width = 1
    def perimeter(self):
        return (self.length+self.width)*2
    def area(self):
        return self.length*self.width

rect = Rectangle(6,3)
print(rect.perimeter())
print(rect.area())