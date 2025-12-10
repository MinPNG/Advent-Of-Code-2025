def decipher(input):
    count = 0
    output = [[char if char == '^' or char == 'S' else '.' for char in line] for line in input]
    height = len(input)
    width = len(input[0])                                                               #Assuming every line has the same len
    for x in range(height - 1): 
        for y in range(width):
            if input[x][y] == 'S' or (output[x][y] == '|' and input[x+1][y] == '.'):     #The particle goes through
                output[x+1][y] = '|'
            if input[x+1][y] == '^' and (output[x][y] == '|' or output[x][y] == 'S'):    #Count whenever the particle splits
                count += 1
                if y > 0:                                                                #Cannot split past the corner of the map
                    output[x+2][y-1] = '|'
                if y < width - 1:
                    output[x+2][y+1] = '|'     
    # return output
    return count

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
#     input = ".......S.......\n\
# ...............\n\
# .......^.......\n\
# ...............\n\
# ......^.^......\n\
# ...............\n\
# .....^.^.^.....\n\
# ...............\n\
# ....^.^...^....\n\
# ...............\n\
# ...^.^...^.^...\n\
# ...............\n\
# ..^...^.....^..\n\
# ...............\n\
# .^.^.^.^.^...^.\n\
# ..............."
    input = input.split('\n')

    output = decipher(input)
    # output = ["".join(line) for line in output]                        #Uncomment this and line 16 for a view of the map       
    # output = "\n".join(output)
    print(output)