def calculator(num1,num2,operations):
    if operations=="+":
        return num1+num2
    elif operations=="-":
        return num1-num2
    elif operations=="*":
        return num1*num2
    elif operations=="/":
        if num2!=0:
            return num1/num2
        else:
            a="division by 0 is not allowed"
            return a
    else:
        b="invalid operation"
        return b
num1=float(input("enter your first number"))
num2=float(input("enter your second number"))
operations=input("enter the operation(+,-,*,/)")

print(calculator(num1,num2,operations))
