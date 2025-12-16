def decipher(input):
    input = input.split('\n')
    input = [list(map(int,line.split(','))) for line in input]
    x_sort = sorted(input,key= lambda x : (x[0],x[1]))
    y_sort = sorted(input,key= lambda x : (x[1],x[0]))
    print(x_sort)
    print(y_sort)
    # size = len(input)
    # max = 1
    # for i in range(size):
    #     for j in range(i,size):
    #         a  = area(input[i],input[j])
    #         max = a if a > max else max
    # return max

def area(a,b):              #Calculate area from a rectangle created by a and b
    height_a,width_a = a
    height_b,width_b = b
    return (abs(height_a - height_b) + 1)*(abs(width_a - width_b) + 1)

def is_valid(a,b,red_tiles,green_tiles):                                                  #2 opposite corner is valid if other 2 are also red/green tiles
    height_a,width_a = a
    height_b,width_b = b
    a2 = (height_a,width_b)
    b2 = (height_b,width_a)
    return (a2 in red_tiles or a2 in green_tiles) and (b2 in red_tiles or b2 in green_tiles)

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
    input = "7,1\n\
11,1\n\
11,7\n\
9,7\n\
9,5\n\
2,5\n\
2,3\n\
7,3"
    output = decipher(input)
    print(output)