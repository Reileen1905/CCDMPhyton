#Users Choice
from PerimeterClass import Perimeter

choice = int(input("Enter 1,2 or 3 to calculate the following :\n1 for Rectangle\n2 for Circle\n3 for Triangle "))

if choice == 1:
    l= int(input("Enter Length:\n"))
    w= int(input("Enter Width:\n"))
    PeriRectObj= Perimeter(l,w,0,0)
    PeriRectObj.PeriRect()

elif choice == 2:
    r=int(input("Insert Radius:\n"))
    CircumfObj= Perimeter(0,0,r,0)
    CircumfObj.Circumf()

elif choice == 3:
    b=int(input("Insert BAse/Sides:\n"))
    PeriTriObj=Perimeter(0,0,0,b)
    PeriTriObj.PeriTri()

else:
    print("Invalid Choice!!")
