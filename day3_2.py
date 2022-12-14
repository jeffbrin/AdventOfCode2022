with open("input.txt") as file:
    lines = file.readlines()
    print(len(lines))

groups = []
group = []
for i, line in enumerate(lines):
    if i % 3 == 0:
        groups.append(group)
        group = []
    group.append(line.split('\n')[0])

groups.append(group)

errors = []
for group in groups[1:]:
    for c in group[0]:
        if c in group[1] and c in group[2]:
            errors.append(c)
            break

sum = 0
for error in errors:
    if error.upper() == error:
        addition = ord(error) - 64 + 26
    else:
        addition = ord(error) - 96

    sum += addition

print(sum)