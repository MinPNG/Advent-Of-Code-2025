def decipher(ranges):                                                                  #Count the size of range
    count = 0
    for range in ranges:
        count += range[1] - range[0] + 1
    return count

def from_string_to_int(range,list):                                                    #Changing to integer for comparison
    int_range = [[int(item[0]),int(item[1])] for item in range]
    int_list = [int(item) for item in list]
    return (int_range,int_list)


def range_handle(ranges):
    output = [ranges[0]]
    for current_range in ranges:
        for range in output:
            if current_range[1] < range[0] or current_range[0] > range[1]:              #Not overlap, move on
                continue
            else:                                                                       #Overlapping, join 2 ranges
                if current_range[0] < range[0]:
                    range[0] = current_range[0]
                if current_range[1] > range[1]:
                    range[1] = current_range[1]
                break
        else:                                                                           #Not overlap to any range, add it to the rang list
            output.append(current_range)
    while (len(output) < len(ranges)):                                                  #Repeat until no overlapping ranges joined (current size is equal previsous size)
        ranges = output
        output = [ranges[0]]
        for current_range in ranges:
            for range in output:
                if current_range[1] < range[0] or current_range[0] > range[1]:          #Not overlap, move on
                    continue
                else:                                                                   #Overlapping, join 2 ranges
                    if current_range[0] < range[0]:
                        range[0] = current_range[0]
                    if current_range[1] > range[1]:
                        range[1] = current_range[1]
                    break
            else:                                                                       #Not overlap to any range, add it to the rang list
                output.append(current_range)
    return output



def is_in_range(range,num):
    if num < range[0] or num > range[1]:
        return False
    return True

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
    # input = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
    input = input.split('\n\n')
    range = input[0]
    range = range.split('\n')
    range = [item.split('-') for item in range]
    list = input[1]
    list = list.split('\n')
    range,list = from_string_to_int(range,list)
    output = decipher(range_handle(range))
    print(output)
