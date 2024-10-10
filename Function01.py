#Create a Function Called Area Of Rectangle
import math
#Defining the function
#5
def AreaOfRectangle():
    length = int(input("Enter Length:\n"))
    width = int(input("Enter Width:\n"))
    area = length*width
    print("Area Of Rectangle is: " , area , "cm squared") 

#Ouside of function
#Here, we CALL the function

AreaOfRectangle()
#Create a Function Called Area of Circle

def AreaOfCircle():
    PI=int(3.14)
    radius = int(input("Enter The Radius:\n"))
    area = math.pi *radius*radius
    print("Area Of Circle is: " , area , "cm squared")

#Outside of Function
#Calling The function

AreaOfCircle()

def TriArea():
    Constant=float(0.5)
    Base= int(input("Enter Base:\n"))
    Height = int(input("Enter Height:\n"))
    area = Constant*Base*Height
    print("Area of Triangle is: " , area , "Squared meter")

#Outside Function
TriArea()



