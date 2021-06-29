import graphics.threedgraphics.cuboid as cb
from graphics.threedgraphics.sphere import sphere_circum as sp
from graphics.threedgraphics.sphere import sphere_area
from graphics import rectangle
from graphics import circle as cr
r=float(input("enter the radius of circle:"))
cr.cir_area(r)
cr.cir_perimeter(r)
l=int(input("enter the length of rectangle="))
b=int(input("enter the breadth of rectangle="))
rectangle.rect_area(l,b)
rectangle.rect_perimeter(l,b)
s=float(input("enter the radius of sphere="))
sp(s)
sphere_area(s)
len=int(input("enter the length of cuboid="))
bre=int(input("enter the breadth of cuboid="))
hei=int(input("enter the height of cuboid="))
cb.cuboid_area(len,bre,hei)
cb.cuboid_perimeter(len,bre,hei)