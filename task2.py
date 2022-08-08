
from secrets import choice


def areaCircle():
    radius=int(input("enter the length of radius"))
    area=2.14*radius*radius
    print(area)
def perCircle():
    radius=int(input("enter the length of radius"))
    per=2.14*2*radius
    print(per)
def areaRect():
    length=int(input("enter the length of rectangle"))
    bredth=int(input("enter the bridth of rectangle")) 
    area=length*bredth
    print(area)
def perRect():
    length=int(input("enter the length of rectangle"))
    bredth=int(input("enter the bridth of rectangle")) 
    per=2*(length+bredth)
    print(per)
def areaSquare():
    sideLen=int(input("enter the length of any of side"))
    area=sideLen*sideLen
    print(area)
def perSquare():
    sideLen=int(input("enter the length of any of side"))
    per=4*sideLen
    print(per)
while True:
    print("1. calculate area of circle ")
    print("2. calculate perimeter of circle ")
    print("3. calculate area of rectangle ")
    print("4. calculate perimeter of rectangle ")
    print("5. calculate area of square ")
    print("6. calculate perimeter of square ")
    print("7. exit ")
    choice=int(input("select a option "))
    if choice==1:
        areaCircle()
    elif choice==2:
        perCircle()
    elif choice==3:
        areaRect()
    elif choice==4:
        perRect()
    elif choice==5:
        areaSquare()
    elif choice==6:
        perSquare()
    else:
        break
        
    
    
    
    
    
    