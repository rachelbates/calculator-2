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
    
  #  if tokens[1] != None :
   #     tokens[1] = float(tokens[1])
  #  if tokens[2] != None :
  #      tokens[2] = float(tokens[2])

    if tokens[0].lower() == 'q' :
        break
    #Addition
    elif tokens[0] == '+' : 
        print(add(float(tokens[1]), float(tokens[2])))
    #Subtraction
    elif tokens[0] == '-':
        print(subtract(float(tokens[1]), float(tokens[2])))
    #Multiply
    elif tokens[0] == '*':
        print(multiply(float(tokens[1]), float(tokens[2])))
#Divide
    elif tokens[0] == '/':
        print(divide(float(tokens[1]), float(tokens[2])))
#Square
    elif tokens[0].lower() == 'square' :
        print(square(float(tokens[1]))) 
    #Cube
    elif tokens[0].lower() == 'cube':
        print(cube(float(tokens[1])))
    #Power
    elif tokens[0].lower() == 'power':
        print(power(float(tokens[1]), float(tokens[2])))
    #Mod
    elif tokens[0].lower() == 'mod':
        print(mod(float(tokens[1]), float(tokens[2])))
    else:
        print("Please enter an operator followed by two integers.")
    

