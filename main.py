'''This program takes 2 number and 1 symbol as input and can perform 3 operations(+,-,/) but with a twist
whenever we enter certain number it gives us wrong calcultion
Author - Vaibhav Rawat
Purpose - Python Problem Solving'''
operator=input('Enter the operator\n')
num1=int(input('Enter the first number\n'))
num2=int(input('Enter the Second number\n'))
if operator=='+':
    if num1==56 or num1==9 and num2==9 or num2==56:
        print(int(77))
    else:
        print(num1+num2)
elif operator=='/':
    if num1==56 or num1==6 and num2==56 or num2==6:
        print(int(4))
    else:    
        print(num1/num2)
elif operator=='*':
    if num1==45 or num1==3 and num2==3 or num2==45:
        print(int(555))
    else:
        print(num1*num2)
else:
    print('Wrong input')
