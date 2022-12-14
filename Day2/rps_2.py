def calculate_round_score(other, result):
    # Loss
    if result == 'X':
        if other == 'A': me = 'C'
        elif other == 'B': me = 'A'
        else: me = 'B'
    # Tie
    elif result == 'Y': 
        me = other
    # Win
    elif result == 'Z':
        if other == 'C': me = 'A'
        elif other == 'A': me = 'B'
        else: me = 'C'
    
    # Convert to int
    other = ord(other) - 64
    me = ord(me) - 64
    shape_score = me

    # win score
    result_score = 0
    if me - other == 1 or me - other == -2:
        result_score = 6
    elif me == other:
        result_score = 3

    return shape_score + result_score
        

with open("C:\\Users\\Jeffrey\\Desktop\\AdventOfCode2022\\Day2\\input.txt", "r") as file:
    rounds = file.readlines()

score = 0
for round in rounds:
    score += calculate_round_score(round[0], round[2])

print(score)