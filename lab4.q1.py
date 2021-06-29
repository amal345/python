class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    
    def area(self):
        return self.l*self.b

    def perimeter(self):
        return 2*(self.l+self.b)

r1=Rectangle(13,5)
print("Area of Rectangle 1 : ",r1.area())
print("Perimeter of Rectangle 1 : ",r1.perimeter())

r2=Rectangle(7,9)
print("Area of Rectangle 2 : ",r2.area())
print("Perimeter of Rectangle 2 : ",r2.perimeter())

if(r1.area() > r2.area()):
    print("Rectangle 1 is bigger ")
else:
    print("Rectangle 2 is bigger ")