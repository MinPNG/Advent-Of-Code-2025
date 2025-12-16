def input_handle(input):
    input = input.split('\n')
    input = [line.split(' ') for line in input]
    light = [line[0][1:-1] for line in input]
    button = [[[int(x) for x in line[i][1:-1].split(',')] for i in range(1,len(line) - 1)] for line in input]
    joltage = [[int(x) for x in line[-1][1:-1].split(',')] for line in input]
    return (light,button,joltage)

def decipher(light,button):
    size = len(light)                               #number of light should be equal number of button schematics

    sum = 0
    for i in range(size):
        sum += find_best_press(light[i],button[i])
    return sum

                                                                        
def find_best_press(light,button_list):                                 #Order of buttons and states don't change the results
    start = [True if char == '#' else False for char in light]          #starting state, (goal state in question)
    goal = [False for _ in light]                                       #goal state, every light is off (starting state in question)
    states = []
    states.append([start])
    visit = []
    visit.append(start)
    i = 0                                                               
    while goal not in visit:                                            #1 cycle = 1 step of toggling
        temp = []
        for state in states[i]:
            for button in button_list:                                  #press all the switch
                next_state  = press(state,button)
                if next_state not in visit:                             #If visited, it means this is not the optimal way
                    visit.append(next_state)
                    temp.append(next_state)
        states.append(temp)
        i += 1
    return len(states) - 1                                              

def press(current_state,button):
    next_state = [state for state in current_state]
    for switch in button:
        next_state[switch] = not current_state[switch]
    return next_state


if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
#     input = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}\n\
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}\n\
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"

    light,button,joltage = input_handle(input)
    print(decipher(light,button))