import json

with open('input.txt', 'r') as file:
    packet_list = file.readlines()

pairs = [(packet_list[i * 3].split("\n")[0], packet_list[i * 3+1].split("\n")[0]) for i, x in enumerate(packet_list[::3])]

class Packet:
    def __init__(self, data: str) -> None:
        self.data = json.loads(data)

    def compareTo(self, other) -> int:
        '''negative number if self is smaller, 0 for equal and positive if self is greater.'''
        return Packet.__compare_lists(self.data, other.data)

    @staticmethod
    def __compare_lists(list1: list, list2: list) -> int:
        i = 0
        while i < len(list1) and i < len(list2):

            self_type = type(list1[i])
            other_type = type(list2[i])

            # Both integers
            if self_type == int and other_type == int:
                if list1[i] != list2[i]:
                    return list1[i] - list2[i]
            # Both lists
            elif self_type == list and other_type == list:
                cmp = Packet.__compare_lists(list1[i], list2[i])
                if cmp != 0:
                    return cmp
            # Self is the only int, convert to list and try again
            elif self_type == int:
                list1[i] = [list1[i]]
                continue
            # Other is the only int, convert to list and try again
            else:
                list2[i] = [list2[i]]
                continue

            # Increment
            i += 1

        # If we've gotten here, length decides
        return len(list1) - len(list2)

good_pairs = []
for i, pair in enumerate(pairs):
    pair_index = i+1

    pair = list(map(lambda x: Packet(x), pair))
    if pair[0].compareTo(pair[1]) <= 0:
        good_pairs.append(pair_index)

print(sum(good_pairs))