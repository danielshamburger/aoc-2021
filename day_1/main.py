def part_1(depths):
    depth_increases = 0

    for index, depth in enumerate(depths):
        if index > 0:
            if depth > depths[index - 1]:
                depth_increases += 1

    return depth_increases


def part_2(depths):
    depth_increases = 0

    for index, depth in enumerate(depths):
        if index < len(depths) - 2 and index > 0:
            previous_window_avg = int(depths[index - 1]) + int(depth) + int(depths[index + 1])
            window_avg = int(depth) + int(depths[index + 1]) + int(depths[index + 2])
            if window_avg > previous_window_avg:
                depth_increases += 1

    return depth_increases


if __name__ == "__main__":
    input = open("input.txt", "r").read()
    depths = input.splitlines()
    
    print(part_1(depths))
    print(part_2(depths))