def calculate_round_score(other, me):
    other = ord(other) - 64
    me = ord(me) - 23 - 64
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