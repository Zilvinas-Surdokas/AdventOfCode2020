import itertools

with open('numbers.txt', 'r') as g:
    data = list(map(int, g.readlines()))

target = 2020
for x in itertools.combinations(data, 2):
    if x[0] + x[1] == target:
        res = x[0] * x[1]
        print("the first number %d the second number %d" % x)
        print(f"The result is: {res}")
