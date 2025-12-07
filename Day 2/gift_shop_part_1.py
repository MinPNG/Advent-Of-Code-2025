def decipher(input):
    sum = 0
    for range in input:
        range = range.split('-')
        lower = range[0]
        upper = range[1]
        tmp = int(lower)
        while (tmp <= int(upper)):
            if is_invalid(tmp):
                print(tmp)
                sum += tmp
            tmp += 1
    return sum

def is_invalid(num):                #Check if first half is equal second half
    string = str(num)
    if len(string) % 2 == 1:
        return False
    mid = len(string)//2
    for i in range(mid):
        if string[i] != string[i+mid]:
            return False
    return True

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
    # input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    input = input.split(',')
    output = decipher(input)
    print(output)