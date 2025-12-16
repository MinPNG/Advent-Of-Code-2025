def input_handle(input):
    input = input.split('\n')
    map = {}
    for line in input:
        line = line.split(' ')
        key = line.pop(0)
        key = key[:-1]
        value = [item for item in line]
        map.update({key:value})
    return map

def decipher(input):
    visited = []
    return search(input,'you',visited)                  

def search(dictionary,current,visited):                 #Deep first search
    count = 0
    next_visited = [item for item in visited]
    if current == 'out':                                #Found exit
        return 1
    if current in visited:                              #Found a loop
        return 0
    next_visited.append(current)
    for next in dictionary[current]:
        if next not in visited:
            count += search(dictionary,next,next_visited)
    return count

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
#     input = "aaa: you hhh\n\
# you: bbb ccc\n\
# bbb: ddd eee\n\
# ccc: ddd eee fff\n\
# ddd: ggg\n\
# eee: out\n\
# fff: out\n\
# ggg: out\n\
# hhh: ccc fff iii\n\
# iii: out"

    input = input_handle(input)
    output = decipher(input)
    # output = ["".join(line) for line in output]                        #Uncomment this and line 16 for a view of the map       
    # output = "\n".join(output)
    print(output)