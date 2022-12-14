with open("input.txt", "r") as file:
    lines = file.readlines()

max_snacks = [0, 0, 0]
current_snacks = 0
for i, line in enumerate(lines):
    if line in lines:
        # If this separates two elves
        if line == "\n":
            # If this elf has the new most snacks
            if current_snacks > max_snacks[-1]:
                max_snacks.append(current_snacks)
                max_snacks.sort(reverse=True)
                max_snacks = max_snacks[:-1]
            
            # Set current snacks to 0 unless it's the last line
            if i != len(lines) - 1:
                current_snacks = 0
        # If this is a calory line
        else:
            current_snacks += int(line)

print(sum(max_snacks))