from collections import deque
stack1 = deque()
stack2 = deque()

def readInput():
    with open("input.txt") as input:
        while True:
            char = input.read(1)
            stack1.append(char)
            stack2.append(char)
            if not char:
                break
            #print(len(stack))

def part1():
    levels = 0
    for i in range (0, len(stack1)-1):
        if stack1[0] == '(':
            levels = levels + 1
        elif stack1[0] == ')':
            levels = levels - 1
        stack1.popleft()
    return levels

def part2():
    levels = 0
    for i in range (0, len(stack2)-1):
        if stack2[0] == '(':
            levels = levels + 1
        elif stack2[0] == ')':
            levels = levels - 1
        #part 2, find the first time he enters the basement
        if levels == -1:
            return i
        stack2.popleft()
    return levels

readInput()
print("The level that santa reaches is: " + str(part1()))
print("The first time santa enters the basement is: " + str(part2() + 1))

