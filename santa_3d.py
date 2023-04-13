import numpy

min_bundle_value = 1

# type1
a = 2
n1 = 2
# type2
b = 3
n2 = 4
# type3
c = 5
n3 = 5

possibilities = []
for i in range(n1 + 1):
    v_a = 1 / a * i
    if v_a >= min_bundle_value:
        possibilities.append((i, 0, 0))
        break
    for j in range(n2 + 1):
        v_b = 1 / b * j
        if v_a + v_b >= min_bundle_value:
            possibilities.append((i, j, 0))
            break
        for k in range(n3 + 1):
            v_c = 1 / c * k
            if v_a + v_b + v_c >= min_bundle_value:
                possibilities.append((i, j, k))
                break

print("Possibilities that Sata can build a bundle:")
print(*possibilities, sep='\n')

memory = numpy.zeros((n1 + 1, n2 + 1, n3 + 1))
for d1 in range(n1 + 1):
    for d2 in range(n2 + 1):
        maximum = 0
        for d3 in range(n3 + 1):
            for i, j, k in possibilities:
                if d1 >= i and d2 >= j and d3 >= k:
                    if maximum < 1 + memory[d1 - i][d2 - j][d3 - k]:
                        maximum = 1 + memory[d1 - i][d2 - j][d3 - k]
            memory[d1][d2][d3] = maximum

print()
print("The maximum number of bundles Santa can pick is:")
print(memory[n1][n2][n3])
