'''''
number = input("Enter a number: ")

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")


    #Task 2

number1= int(input ("Enter number1: "))
number2= int(input ("Enter number2: "))
number3= int(input ("Enter number3: "))

if number1 >= number2 and number1 >= number3:
    print("The largest number is num1")
if number2 >= number1 and number2 >= number3:
    print("The largest number is num2")
if number3 >= number1 and number3 >= number2:
    print("The largest number is num3")
else :
    print("Please enter a whole number")




    #Task 2.A

number1= int(input ("Enter number1: "))
number2= int(input ("Enter number2: "))
number3= int(input ("Enter number3: "))

if number1 <= number2 and number1 <= number3:
    print("The smallest number is num1")
if number2 <= number1 and numbers3<= number3:
    print("The smallest number is num2")
if number3 <= number1 and numbers3 <= number2:
    print("The smallest number is num1")
else :
    print("Please enter a whole number")
    
    '''
    #Task 3

def leap_year():
    year = int(input("Enter a year: "))
    if year % 4==0:
         print ("true")
    else: 
        print ("false")