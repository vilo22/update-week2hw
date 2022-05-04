import math

#1st make the loop work with all the functions
#2nd try to mmke it work step by step with functions 
#3rd export it 

def calculator():

    calculator_active = True

    while calculator_active: 
        answer = input("Welcome to fast calculator! If you want to calculate the area of a house please press '1', if you want to calculate the circumference of a circle please press '2', if you want to exit press '3'")
        if answer == '1':
            area = int(input('please type a number:')) * int(input('Please type another number: '))
            return f'This is the total area of your house: {area}'
    
        elif answer == '2':
            circumference = math.tau * int(input('please type a number:'))
            return f'this is the value of the circumference: {circumference}'

        elif answer == '3':
            calculator_active = False

print(calculator())