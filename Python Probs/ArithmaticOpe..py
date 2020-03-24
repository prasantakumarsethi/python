#Arithmatic Operations are done here..

a= int(input("enter 1st value:-"))
b = int(input("enter 2nd value:-"))
print("Enter Operation you want to operate:-")
print("+ - * / %")

ch = input("")
if ch =='+':
    sum=a+b
    print("addition is",sum)
elif ch =="-":
    sub = a-b
    print("substraction is",sub)
elif ch =="*":
    mult = a*b
    print("multiplication is",mult)
elif ch =="/":
    div = a/b
    print("division is",div)
elif ch =="%":
    mod =a%b
    print("modulous is",mod)
else:
    print('''enter valid input "+  -  *  /  %"''')
