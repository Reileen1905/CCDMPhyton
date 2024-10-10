import math
class Perimeter:

    def __init__(self,l,w,r,b):
        self.length=l
        self.width=w
        self.radius= r
        self.side= b

    def PeriRect(self):
        #length= int(input("Enter Length:\n"))
        #width= int(input("Enter Length :\n"))
        perimeter= self.length+self.width+self.length+self.width
        print("Perimeter of Rectangle is: " , perimeter , "cm squared")

    def Circumf(self):
        constant=int(2)
        #PI=math.pi
        #radius=int(input("Enter Your Radius:\n"))
        perimeter=constant*math.pi*self.radius
        print("Perimeter Of Circlie is " , perimeter , "cm squared")

    def PeriTri(self):
        side= int(input("Enter Side"))

        perimeter= self.side + self.side + self.side
        print("Perimeter Of Triangle is " , perimeter , "cm squared")

#Create Objects Of The Class
#PeriRectObj= Perimeter()
#CircumfObj= Perimeter()
#PeriTriObj= Perimeter()