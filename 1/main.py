left: list[int] = []
right: list[int] = []

with open('input', 'r') as file:
    for line in file:
        split_line = line.split('   ')
        left.append(int(split_line[0]))
        right.append(int(split_line[1].strip()))

left.sort()
right.sort()

distances: list[int] = []
for (a, b) in zip(left, right):
    distances.append(abs(a - b))

total_distance = sum(distances)
print(f'total distance: {total_distance}')

# ---

simularities: list[int] = []
for (i, a) in enumerate(left):
    simularities.append(a)
    counter = 0
    for b in right:
        if a == b:
            counter += 1
    simularities[i] *= counter

simularity_score = sum(simularities)
print(f'simularity score: {simularity_score}')
