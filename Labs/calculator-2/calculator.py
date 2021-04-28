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
    tokens[1] = int(tokens[1])
    tokens[2] = int(tokens[2])
    if tokens[0].lower() == 'q' :
        break
    #Addition
    elif tokens[0] == '+' : 
        print(add(tokens[1], tokens[2]))
    

    

