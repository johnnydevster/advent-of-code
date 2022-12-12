from utils import read_file

lines = read_file("input_9.txt")

rope = [
    {"x": 0, "y": 0},
    {"x": 0, "y": 0},
    {"x": 0, "y": 0},
    {"x": 0, "y": 0},
    {"x": 0, "y": 0},
    {"x": 0, "y": 0},
    {"x": 0, "y": 0},
    {"x": 0, "y": 0},
    {"x": 0, "y": 0},
    {"x": 0, "y": 0},
]


def part_is_adjacent(index):
    part_x = rope[index]["x"]
    part_y = rope[index]["y"]

    # create an array of all adjacent positions
    adjacent_positions = []

    for x in range(-1, 2):
        for y in range(-1, 2):
            pos = {"x": part_x + x, "y": part_y + y}
            adjacent_positions.append(pos)

    def same_x_and_y(obj):
        leading_x = rope[index - 1]["x"]
        leading_y = rope[index - 1]["y"]

        return obj["x"] == leading_x and obj["y"] == leading_y

    return len(list(filter(same_x_and_y, adjacent_positions)))


visited_positions = []


def move_head(direction):
    x = rope[0]["x"]
    y = rope[0]["y"]

    if direction == "R":
        rope[0]["x"] = x + 1

    if direction == "L":
        rope[0]["x"] = x - 1

    if direction == "U":
        rope[0]["y"] = y + 1

    if direction == "D":
        rope[0]["y"] = y - 1

    for i, rope_part in enumerate(list(range(1, len(rope))), start=1):

        current_x = rope[i]["x"]
        current_y = rope[i]["y"]

        leading_x = rope[i - 1]["x"]
        leading_y = rope[i - 1]["y"]

        distance_x = leading_x - current_x
        distance_y = leading_y - current_y

        new_x = current_x
        new_y = current_y

        if not part_is_adjacent(i):

            if distance_x == 1 or distance_x == -1:
                # this means we're moving in the y axis, and new x should be set to same x column
                new_x = leading_x
            if distance_x == 2:
                new_x = current_x + 1
            if distance_x == -2:
                new_x = current_x - 1

            if distance_y == 1 or distance_y == -1:
                new_y = leading_y
            if distance_y == 2:
                new_y = current_y + 1
            if distance_y == -2:
                new_y = current_y - 1
            rope[i]["x"] = new_x
            rope[i]["y"] = new_y

        is_visited = len(list(filter(
            lambda item: item["x"] == rope[-1]["x"] and item["y"] == rope[-1]["y"], visited_positions)))

        if not is_visited:
            visited_positions.append({"x": rope[-1]["x"], "y": rope[-1]["y"]})


for line in [*lines]:
    direction, move_length = line.split()
    for step in range(int(move_length)):
        move_head(direction)


print(f"Part 2: {len(visited_positions)}")

for i, rope_part in enumerate(rope):
    print(f"{i}: {rope_part}")
