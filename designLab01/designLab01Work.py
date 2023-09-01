#
# File:   designLab01Work.py
# Author: 6.01 Staff
# Date:   02-Sep-11
#
# Below are templates for your answers to three parts of Design Lab 1

#-----------------------------------------------------------------------------

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

#-----------------------------------------------------------------------------

class V2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"V2[{self.x}, {self.y}]"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def add(self, v):
        return self.__add__(v)

    def __add__(self, v):
        return V2(self.x + v.x, self.y + v.y)

    def mul(self, s):
        return self.__mul__(s)

    def __mul__ (self, s):
        return V2(self.x * s, self.y * s)

a = V2(1.0, 2.0)
b = V2(2.2, 3.3)
print(a.add(b))

print(a.mul(2))

print(a.add(b).mul(-1))

print(V2(1.1, 2.2) + V2(3.3, 4.4))
#-----------------------------------------------------------------------------

class Polynomial:
    def __init__(self, c):
        self.c = c
    
    
    
    # def __add__(self, p):
        
