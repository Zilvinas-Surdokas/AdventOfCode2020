import itertools

with open('numbers.txt', 'r') as g:
    data = list(map(int, g.readlines()))

target = 2020
for x in itertools.combinations(data, 3):
    if x[0] + x[1] + x[2] == target:
        res = x[0] * x[1] * x[2]
        print("The first number: %d the second number: %d the third number: %d" % x)
        print(f"The result is: {res}")
