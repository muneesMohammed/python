from unittest import result


while True:
    print("1.Add 2 numbers: ")
    print("2.sub 2 numbers: ")
    print("3.mul 2 numbers: ")
    print("4.div 2 numbers: ")
    print("5.exit: ")
    choice=int(input("select an option "))
    if choice==1:
        num1=int(input("enter a 1st number: "))
        num2=int(input("enter a 2st number: "))
        result=num1+num2
        print(result)
    elif choice==2:
        num1=int(input("enter a 1st number "))
        num2=int(input("enter a 2st number "))
        result=num1-num2
        print(result)
    elif choice==3:
        num1=int(input("enter a 1st number "))
        num2=int(input("enter a 2st number "))
        result=num1*num2
        print(result)
    elif choice==4:
        num1=int(input("enter a 1st number "))
        num2=int(input("enter a 2st number "))
        result=num1/num2
        print(result)
    else:
        break
        
           
        
    