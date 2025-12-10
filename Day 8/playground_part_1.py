import math
def input_handle(input):
    input = input.split('\n')
    output = []
    for line in input:
        line = line.split(',')
        output.append(tuple([int(pos) for pos in line]))
    return output

def decipher(input):
    size = len(input)
    circuits = [{i} for i in range(size)]           #Initially, we have n circuit of n boxes

    edges = []                                      #Create set of edges
    for x in range(size):
        edges += [{x,y} for y in range(x+1,size)]
    edges.sort(key = lambda x: get_len(x,input))    #sort edges by length

    # for i in range(10):                             #Do 10 connections for example input
    for i in range(1000):                             #Do 1000 connections
        connect(edges[i],circuits)
    circuits.sort(key = lambda x : len(x),reverse=True)
    return len(circuits[0])*len(circuits[1])*len(circuits[2])

def connect(edge,circuits):
    for circuit in circuits:
        intersection  = edge.intersection(circuit)
        if len(intersection) != 0:     #if the intersection is an empty set, it means that none of 2 nodes is in this circuit
            if len(intersection) == 2:              #if both nodes are in the circuit, do nothing
                break
            if len(intersection) == 1:
                other_node = edge.difference(circuit)
                for circuit_joint in circuits:
                    if other_node.issubset(circuit_joint):
                        circuit.update(circuit_joint)
                        circuits.pop(circuits.index(circuit_joint))
                break



def get_len(edge,input):
    node1,node2 = edge
    return get_distance(input[node1],input[node2])

def get_distance(node1,node2):                       #Return Euclidean distance
    (x1,y1,z1) = node1
    (x2,y2,z2) = node2
    return math.hypot(abs(x1-x2),abs(y1-y2),abs(z1-z2))

if __name__ == "__main__":
    with open("input.txt","r") as input_file:
        input = input_file.read()
#     input = "162,817,812\n\
# 57,618,57\n\
# 906,360,560\n\
# 592,479,940\n\
# 352,342,300\n\
# 466,668,158\n\
# 542,29,236\n\
# 431,825,988\n\
# 739,650,466\n\
# 52,470,668\n\
# 216,146,977\n\
# 819,987,18\n\
# 117,168,530\n\
# 805,96,715\n\
# 346,949,466\n\
# 970,615,88\n\
# 941,993,340\n\
# 862,61,35\n\
# 984,92,344\n\
# 425,690,689"

    input = input_handle(input)
    output = decipher(input)
    
    print(output)