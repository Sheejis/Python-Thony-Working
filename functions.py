def calc():
    num1=int(input("enter a 1st number:"))
    num2=int(input("enter a 2nd number:"))
    cal=int(input("wat do u want: \n 1:addition \n 2:subtraction \n"))
    if cal==1:
        print(num1+num2)
    elif cal==2:
        print(num1-num2)
    else:
        print("wrong entry")

calc()

def calc2():
    num1=int(input("enter a 1st number:"))
    num2=int(input("enter a 2nd number:"))
    cal=int(input("wat do u want: \n 1:divide \n 2:multiply \n"))
    if cal==1:
        print(num1/num2)
    elif cal==2:
        print(num1*num2)
    else:
        print("wrong entry")
    
calc2
