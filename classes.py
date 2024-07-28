#!/bin/python3
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)
        
    def set_x(self, x):
        self.x = max(min(x, 1000), 0)

    def set_y(self, y):
        self.y = max(min(y, 1000), 0)


# class ColorPoint(Point):
#     def __init__ (self, x, y, color):
#         super().__init__(x, y)
#         self.color = color
        
# class Line():
#     def __init__(self, p1, p2):
#         self.a = p1
#         self.b = p2

#     def points(self):
#         return (self.a, self.b)

#     def length(self):
#         return sqrt((self.a.x - self.b.x)**2 + (self.a.y - self.b.y)**2)



# struct myStructure {
#   int myNum;
#   char myLetter;
# };

# int main() {
#   struct myStructure s1;
#   return 0;
# } 



# type date = record
#     month: 1..12;
#     day: 1..31;
#     year: integer
# end;

# var d: date;


# class Dummy: pass

# d1 = Dummy()
# d1.a = 123
# d1.b = 'qwerty'
# d1.c = (666, 999)

# d1.__dict__    
        
# "qwerty".upper()
