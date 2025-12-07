#Assuming the input form the perfect rectangle

def decipher(input):                    
    output = 0
    count = 0
    height = len(input)
    width = len(input[0])                       #Every line will have the same length
    next_input = [[block for block in line] for line in input]       #Variable to store value of the map after removing scrols
    for x in range(height):
        for y in range(width):
            if is_accessible(x,y,input):
                count += 1
                next_input[x][y] = "."
    output += count
    while (count != 0):
        input = [[block for block in line] for line in next_input]   #Removing accessible scrolls
        count = 0
        for x in range(height):
            for y in range(width):
                if is_accessible(x,y,input):
                    count += 1
                    next_input[x][y] = "."
        output += count
    return output

def is_accessible(x,y,matrix):
    height = len(matrix)
    width = len(matrix[0])                      #Every line will have the same length
    #Check if it is a roll
    if matrix[x][y] != '@':                     #If not, then we don't have to check
        return False
    
    adjacent = []
    #Handle corner case:

    if x == 0:
        if y == 0 or y == width - 1:            #Corner only have 3 adjacent positions
            return True
    else:                                       #Not the top line
        if y != width - 1:                      #Not the right column, safe to add top right
            adjacent.append(matrix[x-1][y+1])
        if y != 0:                              #Not the left column , safe to add top left
            adjacent.append(matrix[x-1][y-1])
        adjacent.append(matrix[x-1][y])         #Not the top line,  always safe to add the top block

    if x == height - 1:                        
        if y == 0 or y == width - 1:            #Corner only have 3 adjacent positions
            return True
    else:                                       #Not the bottom line
        if y != width - 1:                      #Not the right column, safe to add bottom right
            adjacent.append(matrix[x+1][y+1])
        if y != 0:                              #Not the left column, safe to add bottom left
            adjacent.append(matrix[x+1][y-1])
        adjacent.append(matrix[x+1][y])         #Not the bottom line, always safe to add the bottom

    if y != 0:                                  #Not the left column, always safe to add the left
        adjacent.append(matrix[x][y-1])        
    if y != width - 1:                          #Not the right column, always safe to add the right  
        adjacent.append(matrix[x][y+1])

    return is_adjacent_4_scrolls(adjacent)

def is_adjacent_4_scrolls(adjacent):            #Check if there are more than n scrolls '@' in the adjacent
    output = [1 if block == '@' else 0 for block in adjacent]
    return (sum(output) < 4)

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
    # input ="..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@."
    input = input.split('\n')
    input = [list(string) for string in input]
    output = decipher(input)
    print(output)