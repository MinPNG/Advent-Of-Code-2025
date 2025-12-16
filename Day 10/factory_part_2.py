def input_handle(input):
    input = input.split('\n')
    input = [line.split(' ') for line in input]
    light = [line[0][1:-1] for line in input]
    button = [[[int(x) for x in line[i][1:-1].split(',')] for i in range(1,len(line) - 1)] for line in input]
    joltage = [[int(x) for x in line[-1][1:-1].split(',')] for line in input]
    return (light,button,joltage)

def decipher(light,button,joltage):
    size = len(light)                               #number of light should be equal number of button schematics

    sum = 0
    for i in range(size):
        best = find_best_press(button[i],joltage[i])
        print(best)
        sum += best
    return sum

                                                                        
def find_best_press(button_list,joltage):           #Order of buttons and states don't change the results
    start = [jolt for jolt in joltage]              #starting state, joltage 
    goal = [0 for _ in joltage]                     #goal state, every light is off (starting state in question)
    states = []
    states.append([start])
    visit = []
    visit.append(start)
    i = 0                                       
    while goal not in visit:                                            #1 cycle = 1 step of toggling
        print(i)
        temp = []
        for state in states[i]:
            for button in button_list:                                  #press all the switch
                next_state  = press(state,button)
                if next_state == goal:
                    return i+1
                if next_state is not None and next_state not in visit:                             #If visited, it means this is not the optimal way
                    visit.append(next_state)
                    temp.append(next_state)
        states.append(temp)
        i += 1
    return len(states) - 1                                              

def press(current_state,button):
    next_state = [state for state in current_state]
    for switch in button:
        if current_state[switch] == 0:
            return None
        next_state[switch] = current_state[switch] - 1                  #decrease joltage by 1
    return next_state


if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
#     input = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}\n\
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}\n\
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"

    light,button,joltage = input_handle(input)
    print(decipher(light,button,joltage))