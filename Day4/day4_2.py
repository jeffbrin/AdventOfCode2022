from helper import read_lines

lines = read_lines("input.txt")

count = 0
for line in lines:
    split_people = line.split(",")
    person_1_sections = split_people[0].split('-')
    person_2_sections = split_people[1].split('-')

    person_1_sections[0] = int(person_1_sections[0])
    person_1_sections[1] = int(person_1_sections[1])
    person_2_sections[0] = int(person_2_sections[0])
    person_2_sections[1] = int(person_2_sections[1])

    first_range = range(person_1_sections[0], person_1_sections[1]+1)
    second_range = range(person_2_sections[0], person_2_sections[1]+1)

    if person_1_sections[0] in second_range or person_1_sections[1] in second_range or person_2_sections[0] in first_range or person_2_sections[1] in first_range:
        count += 1


print(count)