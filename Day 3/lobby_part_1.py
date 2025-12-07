def decipher(input):
    output = 0
    for string in input:
        print(find_joltage(string))
        output += find_joltage(string)
    return output
    

def find_joltage(string):
    array = list(string)
    first_digit,index = find_max(array[:-1])
    second_digit,index = find_max(array[index+1:])              #2nd index does not matter because we only need 2 digitss
    return int(first_digit + second_digit)

def find_max(array):
    print(array)
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
