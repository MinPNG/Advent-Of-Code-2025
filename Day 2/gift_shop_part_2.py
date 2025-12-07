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

def is_invalid(num):                           
    string = str(num)
    l = len(string)
    if l < 2 :
        return False
    if l == 2 or l == 3:                                      #Check first half and 2nd half
        return is_invalid_div_times(num,l)
    if l > 3:                                       #Check every 1/n of string with n is a divisor of length
        for div in get_divisor(l):
            if is_invalid_div_times(num,div):
                return True
    return False

def is_invalid_div_times(num,div):
    string = str(num)
    l = len(string)
    quotient = l//div
    if div == 1 or quotient == 1:
        for i in range(l):
            if string[0] != string[i]:
                return False
    else :
        for check in range(div):
            for step in range(quotient):
                if string[check] != string[check+step*div]:
                    return False
    return True

def get_divisor(len):
    divisors = []
    mid = int(len/2)
    for i in range(1,mid+1):
        if len % i == 0:
            divisors.append(i)
            divisors.append(len//i)
    return divisors

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
    # input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    input = input.split(',')
    output = decipher(input)
    print(output)
    # print(is_invalid(1010))