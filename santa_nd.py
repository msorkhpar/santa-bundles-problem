def add_one(counter, ns, dimensions):
    carry = 1
    for iterator in range(dimensions - 1, -1, -1):
        counter[iterator] += carry
        if counter[iterator] > ns[iterator]:
            counter[iterator] = 0
            carry = 1
        else:
            carry = 0
            break
    return carry


min_bundle_value = 1

# Prompt the user for the number of dimensions for ns and ts
num_dimensions = int(input("Enter the number of dimensions: "))

ts = []
ns = []
for i in range(num_dimensions):
    value = float(input(f"Enter the value for ts[{i}]: "))
    if value < 0:
        raise ValueError("ts must be non-negative")
    elif value > 1:
        value = 1 / value
    ts.append(value)
    value = int(input(f"Enter the value for ns[{i}]: "))
    ns.append(value)

possibilities = []
counter = [0] * num_dimensions
continue_loop = True
while continue_loop:
    bundle_value = 0
    reset = False
    for i in range(num_dimensions):
        v = ts[i] * counter[i]
        bundle_value += v
        if bundle_value >= min_bundle_value:
            p = [0] * num_dimensions
            for j in range(i + 1):
                p[j] = counter[j]
            possibilities.append(p)
            if i == 0:
                continue_loop = False
            else:
                counter[i - 1] += 1
                for j in range(i, num_dimensions):
                    counter[j] = 0
                counter[-1] = -1
            break

    if counter == ns:
        continue_loop = False
    add_one(counter, ns, num_dimensions)

print("Possibilities that Sata can build a bundle:")
print(*possibilities, sep='\n')

memory = {}
index = [0] * num_dimensions
index_key = ""
while True:
    index_key = ""
    for i in index:
        index_key += str(i) + ","
    memory[index_key] = 0
    maximum = 0
    for p in possibilities:
        valid = True
        for i in range(num_dimensions):
            if index[i] < p[i]:
                valid = False
        if not valid:
            continue
        memory_index = ""
        for i in range(num_dimensions):
            memory_index += str(index[i] - p[i]) + ","

        if maximum < 1 + memory[memory_index]:
            maximum = 1 + memory[memory_index]

    memory[index_key] = maximum

    if index == ns:
        break
    if add_one(index, ns, num_dimensions) == 1:
        break

print()
print("The maximum number of bundles Santa can pick is:")
print(memory[index_key])

