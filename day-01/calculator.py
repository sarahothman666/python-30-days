number1 = float(input("Enter the first number:"))
operation = input("Enter the operation:")
number2 = float(input("Enter the second number:"))
if (operation == '+'):
    print (number1 + number2)
elif (operation == '-'):
    print (number1 - number2)
elif (operation == '/'):
    if (number2 == 0):
        print ("Error: The second number must not be zero.")
    else:
        print (number1 / number2)
elif (operation == '*'):
    print (number1 * number2)
else:
    print ("The operation must (+ , - , * , /)")
