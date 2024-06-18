num1=float(input("Enter the First Number:"))
num2=float(input("Enter the Second Number:"))
operator=input("Enter an Arithmetic Operator:")
if operator=="+":
    result=num1+num2
    print(round(result,2))
elif operator=="-":
    result=num1-num2
    print(round(result,2))
elif operator=="*":
    result=num1*num2
    print(round(result,2))
elif operator=="/":
    if num2==0:
        print("Dividing by zero is not possible!")
    else:
        result=num1/num2
        print(round(result,2))
elif operator=="%":
    result=num1%num2
    print(round(result,2))
elif operator=="**":
    result=num1**num2
    print(round(result,2))
elif operator=="//":
    result=num1//num2
    print(round(result,2))