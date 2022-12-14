with open("input.txt", "r") as file:
    string_tree_lines = file.readlines()
    tree_lines = []
    for r, row in enumerate(string_tree_lines):
        string_tree_lines[r] = row.split("\n")[0]
        tree_row = []
        for i, tree in enumerate(string_tree_lines[r]):
            tree_row.append(int(tree))
        tree_lines.append(tree_row)

tree_directional_scores = []
scores = []
for row_number, row in enumerate(tree_lines):
    for col_number, tree in enumerate(row):
        
        column_trees = [x[col_number] for x in tree_lines]
        
        up_trees = column_trees[:row_number]
        down_trees = column_trees[row_number+1:]
        left_trees = row[:col_number]
        right_trees = row[col_number+1:]

        up_distance = 0
        for potential_blocker in up_trees[::-1]:
            up_distance += 1
            if potential_blocker >= tree:
                break
        left_distance = 0
        for potential_blocker in left_trees[::-1]:
            left_distance += 1
            if potential_blocker >= tree:
                break
        down_distance = 0
        for potential_blocker in down_trees:
            down_distance += 1
            if potential_blocker >= tree:
                break
        right_distance = 0
        for potential_blocker in right_trees:
            right_distance += 1
            if potential_blocker >= tree:
                break

        score = down_distance * right_distance * up_distance * left_distance
        scores.append(score)

print(max(scores))