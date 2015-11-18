#Lorenzo Llamas
#hw3q4
import math
x1 = float(input("Enter side #1 of the triangle: "))
x2 = float(input("Enter side #2 of the triangle: "))
x3 = float(input("Enter side #3 of the triangle: "))

isos = x1 == x2 or x1 == x3 or x2 == x3
i_right = x1*math.sqrt(2)
i2_right = x2*math.sqrt(2)
i3_right = x3*math.sqrt(2)

#right_comp = i_right == i2_right or i_right == i3_right or i2_right == i3_right
a= (x2**2 + x3**2 - x1**2) / 2*x2*x3
b= (x3**2 + x1**2 - x2**2) / 2*x3*x1
c= (x1**2 + x2**2 - x3**2) / 2*x1*x2
cosa = math.cos(a)
cosb = math.cos(b)
cosc = math.cos(c)
rev_cosa = (math.acos(cosa) /  0.0174532925) 
rev_cosb = (math.acos(cosb) /  0.0174532925)
rev_cosc = (math.acos(cosc) /  0.0174532925)

right_comp = rev_cosa == rev_cosb or rev_cosa == rev_cosc or rev_cosb == rev_cosc
if(x1 == x2 == x3):
    print(x1,",",x2,",",x3,"forms an equilateral triangle")
elif(isos == True and right_comp == True):
#hyp of isos right has length sqrt(2) * length
    print(x1,",",x2,",",x3,"forms an isosceles right triangle")
elif(isos == True and right_comp == False):
    print(x1,",",x2,",",x3,"forms an isosceles triangle")
else:
    print("These sides for neither an isosceles nor equilateral triangle")

#Extra Credit
    '''
cosa = (b**2 + c**2 - a**2) / 2*b*c
cosb = (c**2 + a**2 - b**2) / 2*c*a
cosc = (a**2 + b**2 - c**2) / 2*a*b
'''
import turtle
wn = turtle.Screen()
tri = turtle.Turtle()

tri.forward(x1)
tri.left(-rev_cosa)
tri.forward(x2)
tri.left(-rev_cosb)
tri.forward(x3)
tri.left(-rev_cosc)
