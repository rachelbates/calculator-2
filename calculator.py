"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# create a while loop that takes an input and assigns it to a variable.
# tokenize the variable into a list
# loop through list to figure out what function and inputs to use
# apply calculator function
# output value

while True :
    user_equation = input('Enter Your Equation. >')
    tokens = user_equation.split(' ')
    
    operation = tokens[0]
    token_one = float(tokens[1])
    if len(tokens) == 3:
        token_two = float(tokens[2])

#if tokens[1] != None :
    #tokens[1] = float(tokens[1])
#if tokens[2] != None :
    #tokens[2] = float(tokens[2])

    if operation.lower() == 'q' :
        break
    #Addition
    elif operation == '+' : 
        print(add(token_one, token_two))
    #Subtraction
    elif operation == '-':
        print(subtract(token_one, token_two))
    #Multiply
    elif operation == '*':
        print(multiply(token_one, token_two))
    #Divide
    elif operation == '/':
        print(divide(token_one, token_two))
    #Square
    elif operation.lower() == 'square' :
        print(square(token_one)) 
    #Cube
    elif operation.lower() == 'cube':
        print(cube(token_one))
    #Power
    elif operation.lower() == 'power':
        print(power(token_one, token_two))
    #Mod
    elif operation.lower() == 'mod':
        print(mod(token_one, token_two))
    else:
        print("Please enter an operator followed by two integers.")
    

