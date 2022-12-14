from enum import Enum

with open('input.txt', 'r') as file:
    map_lines = file.readlines()
    map_lines = map(lambda x: x.split("\n")[0], map_lines)

class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3
    
class Node:

    def __init__(self, element: str, x: int, y: int) -> None:
        self.element = element
        self.x = x
        self.y = y

        self.isStart = element == "S"
        self.isEnd = element == "E"

        if self.isStart:
            self.element = 'a'
        elif self.isEnd:
            self.element = 'z'

        self.visited = False

    def __str__(self) -> str:
        return self.element

class Grid:

    def __init__(self, grid_string_rows: list) -> None:

        self.nodes = []
        for y, row in enumerate(grid_string_rows):
            grid_row = []
            for x, name in enumerate(row):
                grid_row.append(Node(name, x, y))

                # Keep track of start and end
                if grid_row[-1].isStart:
                    self.start = grid_row[-1]
                elif grid_row[-1].isEnd:
                    self.end = grid_row[-1]

            self.nodes.append(grid_row)

    def __str__(self) -> str:
        string = ""
        for row in self.nodes:
            for node in row:
                string += str(node)
            string += "\n"
        return string

    def down(self, node: Node) -> Node:
        '''Returns the node below the current node. None if at the bottom.'''
        if node.y == len(self.nodes) - 1:
            return None

        return self.nodes[node.y+1][node.x]

    def up(self, node: Node) -> Node:
        '''Returns the node above the current node. None if at the top.'''
        if node.y == 0:
            return None

        return self.nodes[node.y-1][node.x]

    def right(self, node: Node) -> Node:
        '''Returns the node to the right of the current node. None if at the very right.'''
        if node.x == len(self.nodes[0]) - 1:
            return None

        return self.nodes[node.y][node.x+1]

    def left(self, node: Node) -> Node:
        '''Returns the node to the left of the current node. None if at the very left.'''
        if node.x == 0:
            return None

        return self.nodes[node.y][node.x-1]

    def bfs(self, starting_node: Node) -> list:
        '''Performs a bfs from start to end and returns a list of directions.'''

        # Reset
        for row in self.nodes:
            for node in row:
                node.visited = False

        to_be_checked = [{"node": starting_node, "path": []}]

        # While there are nodes to be checked
        while len(to_be_checked) > 0:

            # Take the next element in the search
            current = to_be_checked[0]

            # If current is a valid node, check all 4 directions
            if current['node'] is not None and not current['node'].visited:

                current['node'].visited = True

                if current['node'] == self.end:
                    return current

                up = self.up(current['node'])
                if Grid.__is_possible_move(current['node'], up):
                    new = {'node': up, 'path': list(current['path'])}
                    new['path'].append(Direction.Up)
                    to_be_checked.append(new)

                right = self.right(current['node'])
                if Grid.__is_possible_move(current['node'], right):
                    new = {'node': right, 'path': list(current['path'])}
                    new['path'].append(Direction.Right)
                    to_be_checked.append(new)

                left = self.left(current['node'])
                if Grid.__is_possible_move(current['node'], left):
                    new = {'node': left, 'path': list(current['path'])}
                    new['path'].append(Direction.Left)
                    to_be_checked.append(new)

                down = self.down(current['node'])
                if Grid.__is_possible_move(current['node'], down):
                    new = {'node': down, 'path': list(current['path'])}
                    new['path'].append(Direction.Down)
                    to_be_checked.append(new)

            to_be_checked = to_be_checked[1:]

    def shortest_path_from_low_elevation(self) -> list:

        shortest_path = None
        for row in self.nodes:
            for node in row:
                if node.element == 'a':
                    bfs_info = self.bfs(node)

                    # In case of no possible path
                    if bfs_info is None:
                        continue
                    path = bfs_info['path']
                    if shortest_path is None or len(path) < len(shortest_path):
                        shortest_path = path

        return shortest_path

    @staticmethod
    def __is_possible_move(node_from: Node, node_to: Node) -> bool:
        if node_to is None:
            return False

        return ord(node_to.element) - 1 <= ord(node_from.element)
    

grid = Grid(map_lines)
shortest_path = grid.shortest_path_from_low_elevation()
print(len(shortest_path))

