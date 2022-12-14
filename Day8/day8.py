with open("input.txt", "r") as file:
    string_tree_lines = file.readlines()
    tree_lines = []
    for r, row in enumerate(string_tree_lines):
        string_tree_lines[r] = row.split("\n")[0]
        tree_row = []
        for i, tree in enumerate(string_tree_lines[r]):
            tree_row.append(int(tree))
        tree_lines.append(tree_row)

visible_trees = []
for row_number, row in enumerate(tree_lines):
    for col_number, tree in enumerate(row):
        # Outside trees
        if col_number == 0 or row_number == 0 or col_number == len(tree_lines[0])-1 or row_number == len(tree_lines)-1:
            visible_trees.append(tree)
            continue
        else:
            # If the largest tree on the left, right, top, and bottom. If any are smaller
            if max(row[:col_number]) < tree or max(row[col_number+1:]) < tree or max([row[col_number] for row in tree_lines][:row_number]) < tree or max([row[col_number] for row in tree_lines][row_number+1:]) < tree:
                visible_trees.append((row_number, col_number))
