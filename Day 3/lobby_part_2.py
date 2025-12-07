def decipher(input):
    output = 0
    for string in input:
        print(find_joltage(string))
        output += find_joltage(string)
    return output
    

def find_joltage(string):
    array = list(string)
    index = 0
    joltage = ''
    for i in range(11,0,-1):                                   #Here the index matters because we need to find the next digit until 12 digits
        digit,pos = find_max(array[index:-i])
        index += pos + 1                                        #Starting search from the next digit
        joltage += digit

    last_digit,pos = find_max(array[index:])                    #Add the last digit
    joltage += last_digit
    return int(joltage)

def find_max(array):
    max = array[0]
    for value in array:
        if value > max:
            max = value
    return (max,array.index(max))

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
    # input ="987654321111111\n811111111111119\n234234234234278\n818181911112111"
    input = input.split('\n')
    output = decipher(input)
    print(output)
