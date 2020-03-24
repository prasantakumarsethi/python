
print("Enter three numbers:-")
number1 = int(input(''))
number2 = int(input(''))
number3 = int(input(''))

if (number1> number2 and number1> number3):
    print("greater number is :",number1)

elif (number2>number1 and number3< number2):
    print('greatest number is ',number2)

elif (number3>number1 and number3>number2):
    print("greatest number is :",number3)
