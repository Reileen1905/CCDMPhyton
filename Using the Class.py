#As A User
from Classes import Area

l = int(input("Enter Length:\n"))
w = int(input("Enter Width:\n"))
r = int(input("Enter Radius:\n"))
b = int(input("Enter Base:\n"))
h = int(input("Enter Height:\n"))


#Create Objects and Assign Values
RObj=Area(l,w,0,0,0)

#Use Object to access AreaOfRectangle Function
RObj.AreaOfRectangle()  

#Create Objects and Assign Values to AreaOfCircle 
CObj=Area(0,0,r,0,0)

#Use Object to Access AreaOfCircle Func.
#CObj.AreaOfCircle()

#Use Object and Assign Values to AreaOfTriangle
TriObj= Area(0,0,0,b,h)

#Obj. to access AArea of TrObj
TriObj.TriArea()
#Part 2
choice=int(input("Enter Your Number"))
#IF Statement
if choice==1:
    RObj.AreaOfRectangle()
elif choice==2:
    CObj.AreaOfCircle()
elif choice==3:
    TriObj.TriArea()
else:
    print("Sorry!Invalid Option")



