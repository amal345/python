class Rectangle:
    def __init__(self,length,breadth):
        self.__l=length
        self.__b=breadth
    
    def area(self):
        return self.__l*self.__b
    def __lt__(self, other):
        if(self.area()<other.area()):
            return "Area of rectangle 1 is less than rectangle 2"
        else:
            return "Area of rectangle 2 is less than rectangle 1"

r1=Rectangle(9,8)
r2=Rectangle(8,7)
print("Area of Rectangle 1 : ",r1.area())
print("Area of Rectangle 2 : ",r2.area())
print(r1<r2)
