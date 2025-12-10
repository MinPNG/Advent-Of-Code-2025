import re

def decipher(list,operator):
    output = 0
    for index in range(len(operator)):
        if operator[index] == '+':
            output += sum(list[index])
        if operator[index] == '*':
            output += mul(list[index])
    return output

def sum(list):
    sum = 0
    for number in list:
        sum += int(number)
    return sum

def mul(list):
    mul = 1
    for number in list:
        mul *= int(number)
    return mul

def input_handle(input):                                                        #Handle part 2 is different from part 1
    input = input.split('\n')                                                   
    operator_text = input.pop()                                                 #Last line is  +/*
    columns = []
    current_column = []
    operators = []
    for index in range(len(operator_text) - 1,-1,-1):                           #Go from right to left
        column = [line[index] for line in input]                                #Get the column at the current position
        if column := get_num_from_column(column):                               #Skip the empty column
            print(column)
            current_column.append(column) 
        if operator_text[index] == '+' or operator_text[index] == '*':          #When we reach + or *, move to next problem
            operators.append(operator_text[index])
            columns.append(current_column)
            current_column = []

    return (columns,operators)

def get_num_from_column(column):                                               #Get the number based on the current column list, for example [' ',' ','4'] would be 4
    sum = 0
    for char in column:
        sum = sum if char == ' ' else sum*10 + int(char)
    return sum

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
    # input = "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  "
    line,operators = input_handle(input)
    print(decipher(line,operators))
