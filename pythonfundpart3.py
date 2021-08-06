a = 5
print(type(a))
alist = [1,2,'a']
print(type(alist))
heights = [5,4,6,7,3,5]
heights.sort()
print(heights)
alist.reverse()
print(alist)
astring = 'hello world'
bstring = astring.replace('world', 'there!')
print(bstring)
dir(alist)
print(dir(alist))
class Rectangle:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        area = self.height * self.width
        return area
rect1 = Rectangle(12, 10)
print(type(rect1))
rect1.height
print(rect1.height)
rect1.width
print(rect1.width)
rect1.area()
print(rect1.area())
dir(rect1)
print(dir(rect1))
import math
print(type(math))
dir(math)
print(dir(math))
math.log(100,10)
print(math.log(100,10))
math.pi
print(math.pi)
import math as mt

mt.log(100,10)
print(mt.log(100,10)
)