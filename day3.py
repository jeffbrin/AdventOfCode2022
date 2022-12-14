with open("input.txt") as file:
    lines = file.readlines()
    print(len(lines))

errors = []
for line in lines:
    half = len(line) // 2
    first_half = line[:half]
    second_half = line[half:]

    for c in first_half:
        if c in second_half:
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