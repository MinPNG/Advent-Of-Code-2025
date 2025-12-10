import re

def decipher(list,operator):
    output = 0
    for index in range(len(operator)):
        column = [line[index] for line in list]                    #Each '+'/'*' is assigned to columm
        if operator[index] == '+':
            output += sum(column)
        if operators[index] == '*':
            output += mul(column)
    return output

def sum(list):
    sum = 0
    for number in list:
        sum += int(number)
    return sum

def mul(list):
    mul = 1
    print(list)
    for number in list:
        mul *= int(number)
    return mul

def input_handle(input):
    input = re.sub(" +"," ",input)                                          #Simplify multiple space
    input = re.sub(" *\n *","\n",input)                                     #Ignore all space at the start/end of line
    input = re.sub(r" *\Z","",input)                                        #Ignore space at the end of string
    input = input.split('\n')
    operator_text = input.pop()                                             #Last line is +/*
    input = [line.split(" ") for line in input]                             #Get list of number from string
    operators = operator_text.split(" ")
    return (input,operators)

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
    # input = "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  "
    line,operators = input_handle(input)
    print(decipher(line,operators))