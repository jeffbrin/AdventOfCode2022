import json

with open('input.txt', 'r') as file:
    packet_list = file.readlines()

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

    def __str__(self) -> str:
        return str(self.data)[2:-2]

def sort_packets(packets: list) -> list:
    # Insertion sort
    for i in range(0, len(packets)-1):
        # i is the first non-sorted item
        j = i+1
        while j > 0:
            if packets[j].compareTo(packets[j-1]) < 0:
                swap(packets, j-1, j)
            j -= 1

    return packets

def swap(lst: list, i: int, j: int) -> None:
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

packets_data = [packet_data.split("\n")[0] for packet_data in packet_list if packet_data != "\n"]

packets = sort_packets(list(map(lambda x: Packet(x), packets_data)))

signal = 1
for i, x in enumerate(packets):
    print(str(x))
    if str(x) == "[[2]]" or str(x) == "[[6]]":
        signal *= i+1

print(signal)