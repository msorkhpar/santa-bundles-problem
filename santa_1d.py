import numpy

min_bundle_value = 1
# type1
a = 0.5
n1 = 5


possibilities = []
for i in range(n1 + 1):
    if (a * i) >= min_bundle_value:
        possibilities.append(i)
        break

print("Possibilities that Sata can build a bundle:")
print(*possibilities, sep='\n')
print()

memory = numpy.zeros((n1 + 1))
maximum = 0
for d1 in range(n1 + 1):
    for i in possibilities:
        if d1 >= i:
            if maximum < 1 + memory[d1 - i]:
                maximum = 1 + memory[d1 - i]
    if maximum != 0:
        memory[d1] = maximum
        print(memory)

print()
print("Final matrix is:")
print(memory)

print()
print("The maximum number of bundles Santa can pick is:")
print(memory[n1])
