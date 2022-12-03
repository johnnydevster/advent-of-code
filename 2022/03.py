from utils import read_file

# Item priority
#
# Lowercase a-z: 1-26
# Uppercase A-Z: 27-52

alphabet = "abcdefghijklmnopqrstuvwxyz"

priorities = {}

for i, letter in enumerate(alphabet, start=1):
    priorities[letter] = i
    priorities[letter.upper()] = i + 26


def find_common_letter(array):
    first_string = array[0]
    the_rest = array[1:]

    # Loop through each letter in the first string of the array
    for letter in first_string:
        condition = True

        # Loop through the rest of the strings.
        # If the letter isn't found, break the loop early
        for other_string in the_rest:
            if letter not in other_string:
                condition = False
                break

        # If condition still holds true after the loop, the letter is common across all provided strings.
        if condition:
            return letter


def find_priority(letter):
    return priorities[letter]


part_one_sum = 0

groups = []
current_group = []

lines = read_file("input_3.txt")

for i, line in enumerate(lines):
    # Part 1
    half_string_length = int(len(line) / 2)
    string_halves = [line[0:half_string_length], line[half_string_length:]]

    common_letter = find_common_letter(string_halves)
    priority = find_priority(common_letter)
    part_one_sum += priority

    # Part 2, divide elves into groups
    current_group.append(line[:-1])
    if len(current_group) == 3:
        groups.append(current_group)
        current_group = []


part_two_sum = 0

for group in groups:
    common_letter = find_common_letter(group)
    priority = find_priority(common_letter)
    part_two_sum += priority

print(f"Part 1 solution: {part_one_sum}")

print(f"Part 2 solution: {part_two_sum}")
