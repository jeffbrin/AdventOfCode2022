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

    lowest_section = min(person_1_sections[0], person_2_sections[0])
    highest_section = max(person_1_sections[1], person_2_sections[1])

    if (lowest_section == person_1_sections[0] and highest_section == person_1_sections[1]) or (lowest_section == person_2_sections[0] and highest_section == person_2_sections[1]):
        print(line)
        count += 1

print(count)