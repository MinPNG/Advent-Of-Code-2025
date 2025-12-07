import enum
import os

def decipher(start,input):
    password = 0
    for rotation in input:
        left,rotate = split_rotation(rotation)
        if left:
            start = rotate_left(start,rotate)
        if not left:
            start = rotate_right(start,rotate)
        if start == 0:
            password += 1
    return password

def split_rotation(rotation):
    return (rotation[0] == 'L', int(rotation[1:]))

def rotate_left(start,rotate):
    rotate = rotate % 100
    return start - rotate if start - rotate >= 0 else 100 + start - rotate

def rotate_right(start,rotate):
    rotate = rotate %100
    return start + rotate if start + rotate < 100 else start + rotate - 100

if __name__ == '__main__':
    with open("input.txt","r") as input_file:
        input = input_file.read()
        input = input.split('\n')
    # input = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
    output = decipher(50,input)
    print(output)