def decipher(input):
    output = [[char if char == '^' or char == 'S' else '.' for char in line] for line in input]
    height = len(input)
    width = len(input[0])                                                                   #Assuming every line has the same len
    for x in range(height - 1): 
        for y in range(width):
            if input[x][y] == 'S':
                y_root = y
            if (input[x][y] == 'S' or output[x][y] == '|') and input[x+1][y] == '.':               #The particle goes through
                output[x+1][y] = '|'
            if input[x+1][y] == '^' and (output[x][y] == '|' or output[x][y] == 'S'):       #Count whenever the particle splits
                if y > 0:                                                                   #Cannot split past the corner of the map
                    output[x+2][y-1] = '|'
                if y < width - 1:
                    output[x+2][y+1] = '|'     

    posibilities = [[0 for char in line] for line in output]
    for x in range(height - 1,0,-1):                                                        #Loop from the end of the map
        for y in range(width):
            if x == height - 1  and output[x][y] == '|':                                    # only 1 timeline at the end
                posibilities[x][y] = 1
                continue
            if output[x][y] == '|' and output[x+1][y] == '|':                               #Goes in straight line, timeline count remains
                posibilities[x][y] = posibilities[x+1][y]
            if output[x][y] == '|' and output[x+1][y] == '^':                               #If splitting, it can either go left or right => timelines of both side combine
                if y > 0:                                                                   #Cannot split past the corner of the map
                    posibilities[x][y] += posibilities[x+2][y-1]
                if y < width - 1:
                    posibilities[x][y] += posibilities[x+2][y+1]
    #return output
    return posibilities[1][y_root]                                                          #Root timeline should be here


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
    # output = ["".join(line) for line in output]       #Uncomment this and line 30 for a view of the map
    # output = "\n".join(output)
    print(output)