with open("input.txt", 'r') as file:
    # Format input
    instructions = file.readlines()
    for i, instruction in enumerate(instructions):
        split_instr = instruction.split()
        instructions[i] = {
            "instr": split_instr[0], 
            "val": int(split_instr[1]) if split_instr[0] != "noop" else None
            }

cycle = 0
x = 1
cycle_check_start = 20
cycle_increment_check = 40
signal_strengths = []
for instruction in instructions:
    if instruction['instr'] == "noop":
        cycle += 1
        # Track signal strength
        if (cycle - cycle_check_start) % cycle_increment_check == 0:
            signal_strengths.append(cycle * x)
    else:
        for _ in range(2):
            cycle += 1
            # Track signal strength
            if (cycle - cycle_check_start) % cycle_increment_check == 0:
                signal_strengths.append(cycle * x)
        x += instruction['val']

print(sum(signal_strengths))