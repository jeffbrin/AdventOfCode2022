from enum import Enum

class NodeType(Enum):
    Rock = "#"
    SandOrigin = "+"
    Sand = "o"
    Air = "."



class Node:
    def __init__(self, x: int, y: int, type = NodeType.Air) -> None:
        self.x = x
        self.y = y
        self.type = type

    def __str__(self) -> str:
        return self.type.value

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class RockStructure:

    def __init__(self, min_x: int, min_y: int, max_x: int, max_y: int, starting_x: int, starting_y: int) -> None:
        '''Creates an empty grid of air cells'''
        self.nodes = []
        for y in range(min_y, max_y+1):
            line = []
            for x in range(min_x, max_x+1):
                if x == starting_x and y == starting_y:
                    line.append(Node(x, y, NodeType.SandOrigin))
                else:
                    line.append(Node(x, y))
            self.nodes.append(line)
        self.min_y = min_y
        self.min_x = min_x
        self.height = max_y - min_y
        self.starting_x = starting_x - min_x
        self.starting_y = starting_y - min_y

    def __str__(self) -> str:
        string = ""
        for i, row in enumerate(self.nodes):
            string += str(i)
            for node in row:
                string += str(node)
            string += "\n"

        return string

    def add_line(self, x_positions: list, y_positions: list):
        for i in range(len(x_positions)-1):
            # Check which value will change, x or y
            if x_positions[i] != x_positions[i+1]:
                
                x1 = min(x_positions[i:i+2])
                x2 = max(x_positions[i:i+2])

                # Loop through x position diff
                for x in range(x1, x2+1):
                    self.nodes[y_positions[i] - self.min_y][x - self.min_x].type = NodeType.Rock
            else:

                y1 = min(y_positions[i:i+2])
                y2 = max(y_positions[i:i+2])

                # Loop through y position diff
                for y in range(y1, y2+1):
                    self.nodes[y - self.min_y][x_positions[i] - self.min_x].type = NodeType.Rock

    def add_sand(self) -> bool:
        '''Returns true if the sand came to a rest, false otherwise.'''
        # Start at the starting x and y
        sand_position = Vector(self.starting_x, self.starting_y)
        at_rest = False

        while not at_rest and sand_position.y < self.height:
            if self.nodes[sand_position.y+1][sand_position.x].type == NodeType.Air:
                sand_position.y += 1
            elif self.nodes[sand_position.y+1][sand_position.x-1].type == NodeType.Air:
                sand_position.y += 1
                sand_position.x -= 1
            elif self.nodes[sand_position.y+1][sand_position.x+1].type == NodeType.Air:
                sand_position.y += 1
                sand_position.x += 1
            else:
                at_rest = True
                self.nodes[sand_position.y][sand_position.x].type = NodeType.Sand

        return at_rest

with open("input.txt", 'r') as file:
    lines = file.readlines()


rock_lines = []
starting_x = 500
starting_y = 0
min_x = starting_x
max_x = starting_x
min_y = starting_y
max_y = starting_y
for line in lines:
    split_line = line.split("->")
    x_positions = [int(x.split(',')[0]) for x in split_line]
    y_positions = [int(x.split(',')[1]) for x in split_line]

    for x, y in zip(x_positions, y_positions):
        if x < min_x: min_x = x
        if x > max_x: max_x = x
        if y < min_y: min_y = y
        if y > max_y: max_y = y

    rock_lines.append({'x': x_positions, 'y': y_positions})


structure = RockStructure(min_x, min_y, max_x, max_y, starting_x, starting_y)

for line in rock_lines:
    structure.add_line(line['x'], line['y'])

at_rest = True
sand = 0
while at_rest:
    at_rest = structure.add_sand()
    if at_rest:
        sand += 1

print(structure)
print(sand)