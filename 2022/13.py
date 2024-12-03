from utils import read_file
from ast import literal_eval
from itertools import zip_longest

lines = read_file("input_13_test.txt")

packet_pairs = []

pair = []

for line in lines:
    if line == "\n":
        left, right = pair
        pair = list(zip_longest(left, right))
        packet_pairs.append(pair)
        pair = []
        continue
    packet = literal_eval(line.strip("\n"))
    pair.append(packet)


def compare_values(left, right):
    if left == None:
        return True
    if right == None:
        return False
    if type(left) == int and type(right) == int:
        if left != right:
            return left < right
    if type(left) == list and type(right) == list:
        zipped = list(zip_longest(left, right))
        for pair in zipped:
            comparison = compare_values(*pair)
            if comparison != None:
                return comparison
    if type(left) == int and type(right) == list:
        zipped = list(zip_longest([left], right))
        for pair in zipped:
            comparison = compare_values(*pair)
            if comparison != None:
                return comparison
    if type(left) == list and type(right) == int:
        zipped = list(zip_longest(left, [right]))
        for pair in zipped:
            comparison = compare_values(*pair)
            if comparison != None:
                return comparison


indexes = []

for i, packet_pair in enumerate([packet_pairs[6]], start=1):
    for left, right in packet_pair:
        if (compare_values(left, right) == True):
            indexes.append(i)
            break

print(sum(indexes))
pass
