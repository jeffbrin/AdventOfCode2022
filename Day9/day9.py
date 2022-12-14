with open("input.txt", "r") as file:
    steps = file.readlines()

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def move_tail(head_position: Vector, tail_position: Vector):

    y_dist = abs(tail_position.y - head_position.y)
    x_dist = abs(tail_position.x - head_position.x)

    # If they aren't in the same line
    if x_dist > 1 or (y_dist > 1 and x_dist == 1):
        tail_position.x += (head_position.x - tail_position.x) // x_dist
    if y_dist > 1 or (x_dist > 1 and y_dist == 1):
        tail_position.y += (head_position.y - tail_position.y) // y_dist

def move_head(direction: str, head_position: Vector):
    if direction == "R":
        head_position.x += 1
    elif direction == "L":
        head_position.x -= 1
    elif direction == "U":
        head_position.y += 1
    elif direction == "D":
        head_position.y -= 1

positions = []
for x in range(10):
    positions.append(Vector(0, 0))

# Store all the visited positions
visited_positions = {(positions[-1].x, positions[-1].y)}

for step_group in steps:
    split_step_group = step_group.split()
    direction = split_step_group[0]
    amount = int(split_step_group[1])

    for x in range(amount):
        move_head(direction, positions[0])
        # Move
        for pos in range(10-1):
            head_position = positions[pos]
            tail_position = positions[pos+1]
            move_tail(head_position, tail_position)
        visited_positions.add((positions[-1].x, positions[-1].y))
    print(list(map(lambda pos : (pos.x, pos.y), positions)))

print(len(visited_positions))
        