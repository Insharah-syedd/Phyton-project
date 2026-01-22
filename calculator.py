#Calulator
num1=float(input("Enter a first number"))
num2=float(input("Enter a second number"))
operator=input("Enter operator (add,sum,mul.div,mod):")

if operator == "add":
    print(num1+num2)
elif operator =="sum":
    print(num1-num2)
elif operator == "mul":
    print(num1*num2)
elif operator == "div":
    if num2 !=0:
        print("Result:",num1/num2)
    else:   
        print("Error: Divison by Zero")
elif operator == "mod":
    if num2 !=0:
        print("Result:",num1%num2)
    else:
        print("Error: moduls by zero")
else:
    print("Invalid Operator")