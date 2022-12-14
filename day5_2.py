class Stack:
    def __init__(self) -> None:
        self.elements = []

    def push(self, elements):
        for element in elements[::-1]:
            self.elements.append(element)

    def pop(self, quantity):
        if len(self.elements) == 0:
            raise Exception("Can not pop an empty stack.")

        items = []
        for i in range(quantity):
            items.append(self.elements.pop())

        return items

    def top(self):
        if len(self.elements) == 0:
            raise Exception("Can not use top() on an empty stack.")

        return self.elements[-1]

with open("input.txt") as file:
    lines = file.readlines()

stacks = []
for i in range(9):
    stacks.append(Stack())

# Add each stack crate to the stacks
for line in lines[7::-1]:
    for x in range(9):
        character = line[1 + x * 4]
        if character != " ":
            stacks[x].push(character)

instructions = lines[9:]
for instruction in instructions:
    split_instructions = instruction.split()
    quantity = int(split_instructions[1])
    origin = int(split_instructions[3]) - 1
    to = int(split_instructions[5]) - 1

    if quantity > 1:
        print()

    stacks[to].push(stacks[origin].pop(quantity))

message = ""
for stack in stacks:
    message += stack.top()

print(message)