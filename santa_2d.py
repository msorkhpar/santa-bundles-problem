import numpy

min_bundle_value = 1
# type1
a = 0.9
n1 = 2
# type2
b = 0.1
n2 = 2

possibilities = []

for i in range(n1 + 1):
    if (a * i) >= min_bundle_value:
        possibilities.append((i, 0))
        break
    for j in range(n2 + 1):
        if (a * i) + (b * j) >= min_bundle_value:
            possibilities.append((i, j))
            break

print("Possibilities that Sata can build a bundle:")
print(*possibilities, sep='\n')
print()

memory = numpy.zeros((n1 + 1, n2 + 1))
for d1 in range(n1 + 1):
    maximum = 0
    for d2 in range(n2 + 1):
        for i, j in possibilities:
            if d1 >= i and d2 >= j:
                if maximum < 1 + memory[d1 - i][d2 - j]:
                    maximum = 1 + memory[d1 - i][d2 - j]
        if maximum != 0:
            memory[d1][d2] = maximum
            print(memory)
            print("*" * 20)

print()
print("Final matrix is:")
print(memory)

print()
print("The maximum number of bundles Santa can pick is:")
print(memory[n1][n2])
