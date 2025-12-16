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
    return advance_search(input,'svr',[],'dac')*advance_search(input,'dac',[],'fft')*advance_search(input,'fft',[],'out') + advance_search(input,'svr',[],'fft')*advance_search(input,'fft',[],'dac')*advance_search(input,'dac',[],'out')

def advance_search(dictionary,current,visited,dest):    #Deep first search for a specific destination rather than 'out'
    print(current)
    count = 0
    if current == dest:                                
        return 1
    if current == 'out':                                #Reach 'out' before dest, not count
        return 0
    if current in visited:                              #Found a loop
        print('dead end')
        return 0

    
    for next in dictionary[current]:
        if next not in visited:
            count += advance_search(dictionary,next,visited + [current],dest)
    return count




if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
#     input = "svr: aaa bbb\n\
# aaa: fft\n\
# fft: ccc\n\
# bbb: tty\n\
# tty: ccc\n\
# ccc: ddd eee\n\
# ddd: hub\n\
# hub: fff\n\
# eee: dac\n\
# dac: fff\n\
# fff: ggg hhh\n\
# ggg: out\n\
# hhh: out"

    input = input_handle(input)
    output = decipher(input)
    # output = ["".join(line) for line in output]                        #Uncomment this and line 16 for a view of the map       
    # output = "\n".join(output)
    print(output)