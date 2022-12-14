with open("input.txt", 'r') as file:
    # Format input
    instructions = file.readlines()
    for i, instruction in enumerate(instructions):
        split_instr = instruction.split()
        instructions[i] = {
            "instr": split_instr[0], 
            "val": int(split_instr[1]) if split_instr[0] != "noop" else None
            }

def x_draw_position(cycle: int) -> int:
    return cycle % 40

def pixel_to_draw(cycle: int, x: int) -> bool:
    x_draw_pos = x_draw_position(cycle-1)
    return "#" if x_draw_pos == x or x_draw_pos == x - 1 or x_draw_pos == x + 1 else "."

cycle = 0
x = 1

for instruction in instructions:
    if instruction['instr'] == "noop":
        cycle += 1
        print(pixel_to_draw(cycle, x), end="")
        if cycle % 40 == 0:
            print()
    else:
        for _ in range(2):
            cycle += 1
            print(pixel_to_draw(cycle, x), end="")
            if cycle % 40 == 0:
                print()
            
        x += instruction['val']
    
