from utils import read_file


def create_range_from_string(string):
    numbers = string.split("-")
    start = int(numbers[0])
    stop = int(numbers[1]) + 1

    return range(start, stop)


def compare_range_containment(array):
    for i, current_range in enumerate(array):
        print(f"current range: {current_range}")
        for i_2, other_range in enumerate(array):
            # Don't compare the same values against each other
            if i == i_2:
                continue
            print(f"compare {current_range} to {other_range}")
            is_contained = True

            for number in current_range:
                if number not in other_range:
                    print(f"{number} is not contained in {other_range}, breaking")
                    is_contained = False
                    break
            if is_contained:
                return True


def compare_range_overlap(array):
    for i, current_range in enumerate(array):
        print(f"current range: {current_range}")
        for i_2, other_range in enumerate(array):
            # Don't compare the same values against each other
            if i == i_2:
                continue
            print(f"compare {current_range} to {other_range}")

            for number in current_range:
                if number in other_range:
                    print(f"{number} overlaps with {other_range}")
                    return True


contained_groups = 0
overlapping_groups = 0

lines = read_file("input_4.txt")

for line in lines:
    split = line.split(",")

    ranges = []

    for r in split:
        ranges.append(create_range_from_string(r))

    if compare_range_containment(ranges):
        contained_groups += 1

    if compare_range_overlap(ranges):
        overlapping_groups += 1

print(f"Part 1 answer: {contained_groups}")
print(f"Part 2 answer: {overlapping_groups}")
