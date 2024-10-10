#Create a Class called are Area
#This class will contain all
#--functions to calculate Area
import math
class Area:

    #Create a Constructor
    #This is a function also reffered to 
    #as _init_
    def __init__(self,l,w,r,b,h):
        self.length = l
        self.width = w
        self.radius = r
        self.Base = b
        self.Height = h

    def AreaOfRectangle(self):
        #length = int(input("Enter Length:\n"))
        #width = int(input("Enter Width:\n"))
        area = self.length*self.width
        print("Area Of Rectangle is: " , area , "cm squared") 

    def AreaOfCircle(self):
        #PI=int(3.14)
        #radius_1 = int(input("Enter The Radius:\n"))
        #adius_2 = int(input("Enter Radius_1:\n"))
        area = math.pi *self.radius*self.radius
        print("Area Of Circle is: " , area , "cm squared")

    def TriArea(self):
        Constant=float(0.5)
        #Base= int(input("Enter Base:\n"))
        #Height = int(input("Enter Height:\n"))
        area =Constant*self.Base*self.Height
        print("Area of Triangle is: " , area , "Squared meter")
    
        #End Of Functions

#Create OBJECTS here outside of the CLASS
RObj = Area()
CObj = Area()
TriObj = Area()


