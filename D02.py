from functools import reduce

with open("D02.txt") as file:
    input = list(map(lambda y: (y[0], int(y[1])),
                     (map(lambda x: x.split(" "), file.read().splitlines()))))


value = reduce(lambda a, b:
               [a[0] + b[1], a[1]] if b[0] == "forward"
               else [a[0], a[1] + b[1]] if b[0] == "down"
               else [a[0], a[1] - b[1]], input, (0, 0))

value2 = reduce(lambda a, b:
                [a[0] + b[1], a[1]+a[2]*b[1], a[2]] if b[0] == "forward"
                else [a[0], a[1], a[2]+b[1]] if b[0] == "down"
                else [a[0],a[1], a[2] - b[1]], input, (0, 0, 0))

print(value[0] * value[1])
print(value2[0] * value2[1])