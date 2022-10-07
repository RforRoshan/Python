import math
a=float(input("Enter the angle in degree: "))
a=a*math.pi/180
b=float(input("Enter the Distance in meter: "))
h=math.tan(a)*b
h=h*3.281
print("Height of a Tower in Feet= %0.2f" %h)