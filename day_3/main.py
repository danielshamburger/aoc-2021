def part_1(commands):
    gamma = ""
    epsilon = ""

    for i in range(len(commands[0])):
        sum = 0
        
        for command in commands:
            sum += int(command[i])
        
        if sum >= len(commands) / 2: 
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
        
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    raw_input = open("input.txt", "r").read()
    commands = raw_input.splitlines()

    print(part_1(commands))