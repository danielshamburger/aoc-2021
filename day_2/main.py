def solve(commands):
    horizontal = 0
    depth = 0
    aim = 0

    for command in commands:
        parsed_command = command.split()
        direction = parsed_command[0]
        value = parsed_command[1]

        if direction == "forward":
            horizontal += int(value)
            depth += (aim * int(value))
        elif direction == "down":
            aim += int(value)
        elif direction == "up":
            aim -= int(value)

    return horizontal * depth
            

if __name__ == "__main__":
    raw_input = open("input.txt", "r").read()
    commands = raw_input.splitlines()

    print(solve(commands))