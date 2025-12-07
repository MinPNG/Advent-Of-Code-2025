import enum
import os

def decipher(start,input):
    password = 0
    for rotation in input:
        left,rotate = split_rotation(rotation)
        if left:
            start,password = rotate_left(start,rotate,password)
        if not left:
            start,password = rotate_right(start,rotate,password)
        if start == 0:
            password += 1
        print (start,password)
    return password

def split_rotation(rotation):
    return (rotation[0] == 'L', int(rotation[1:]))

def rotate_left(start,rotate,password):                         #In addition to part 1 code, password is increase if it passed 0
    password += rotate // 100
    rotate = rotate % 100
    password += 1 if start - rotate < 0 and start != 0 else 0   #If it starts the rotation at 0, it's already counted at the previous loop
    return (start - rotate,password) if start - rotate >= 0 else (100 + start - rotate,password)

def rotate_right(start,rotate,password):                        #In addition to part 1 code, password is increase if it passed 0
    password += rotate // 100
    rotate = rotate % 100
    password += 1 if start + rotate > 100 else 0
    return (start + rotate,password) if start + rotate < 100 else (start + rotate - 100,password)

if __name__ == '__main__':
    with open("input.txt","r") as input_file:
        input = input_file.read()
        input = input.split('\n')
    # input = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
    output = decipher(50,input)
    print(output)