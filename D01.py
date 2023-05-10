with open("D01.txt") as file:
    input = list(map(int, file.read().splitlines()))


def Day01(inp):
    return len(list(filter(lambda x: x[0] < x[1], inp)))


print(Day01(zip(input, input[1:])))
print(Day01(zip(input, input[3:])))
