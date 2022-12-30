from utils import read_file
from collections import defaultdict

lines = read_file("input_12.txt")

alphabet = 'abcdefghijklmnopqrstuvwxyz'

elevation_scores = {letter: i for i, letter in enumerate(alphabet, start=1)}

grid = defaultdict(list)

start = {}

end = {}

for y, line in enumerate(list(lines)):
    stripped_line = line.strip("\n")
    for x, letter in enumerate(stripped_line):
        if letter == "S":
            start["x"] = x
            start["y"] = y
            grid[x] = [*grid[x], {"el": 1, "score": 999}]
        if letter == "E":
            end["x"] = x
            end["y"] = y
            grid[x] = [*grid[x], {"el": 26, "score": 999}]
        if letter != "S" and letter != "E":
            grid[x] = [
                *grid[x], {"el": elevation_scores[letter], "score": 999}]

queue = [{
    "x": end["x"],
    "y": end["y"],
    "el": 26,
    "score": 0
}]

x_limit = len(grid.keys())
y_limit = len(grid[1])


def is_valid_pos(pos, current):
    el_diff = current["el"] - pos["el"]
    print(f"diff: {el_diff}")
    is_not_in_queue = len(list(filter(lambda item: pos["x"] ==
                                      item["x"] and pos["y"] == item["y"], queue))) == 0

    return el_diff <= 1 and is_not_in_queue


for current in queue:
    print(f"current: {current}")
    adjacent = []
    score = current["score"] + 1
    curr_x = current["x"]
    curr_y = current["y"]

    left_x, left_y = (curr_x - 1, curr_y)
    right_x, right_y = (curr_x + 1, curr_y)
    top_x, top_y = (curr_x, curr_y - 1)
    bottom_x, bottom_y = (curr_x, curr_y + 1)

    if left_x > -1:
        left = {"x": left_x, "y": left_y,
                "el": grid[left_x][left_y]["el"], "score": score}
        if is_valid_pos(left, current):
            adjacent.append(left)

    if right_x < x_limit:
        right = {"x": right_x, "y": right_y,
                 "el": grid[right_x][right_y]["el"], "score": score}
        if is_valid_pos(right, current):
            adjacent.append(right)

    if top_y > -1:
        top = {"x": top_x, "y": top_y,
               "el": grid[top_x][top_y]["el"], "score": score}
        if is_valid_pos(top, current):
            adjacent.append(top)

    if bottom_y < y_limit:
        bottom = {"x": bottom_x, "y": bottom_y,
                  "el": grid[bottom_x][bottom_y]["el"], "score": score}
        if is_valid_pos(bottom, current):
            adjacent.append(bottom)

    queue.extend(adjacent)
    print(f"adjacent values: {adjacent}")
    print(" ")

for pos in queue:
    x = pos["x"]
    y = pos["y"]
    score = pos["score"]

    grid[x][y]["score"] = score

""" f = open("output.txt", "w") """

""" temp_row = ""
for key in list(grid.keys()):
    whitespace = (4 - len(str(key))) * " "
    temp_row += str(key) + whitespace

f.write(temp_row + "\n")
temp_row = ""

for i, y_pos in enumerate(grid[0]):
    for key in list(grid.keys()):
        whitespace = (4 - len(str(grid[key][i]["score"]))) * " "
        temp_row += str(grid[key][i]["score"]) + whitespace
    f.write(temp_row + "\n")
    temp_row = ""
f.close() """


print(" ")
print(end)
print(" ")


positions = [start, *list(filter(lambda item: item["el"] == 1, queue))]
a_steps = []

print(" ")


def is_visited(pos, visited):
    return len(list(filter(lambda item: item["x"] == pos["x"] and item["y"] == pos["y"], visited))) > 0


for current_pos in positions:
    visited = []
    steps = 0
    while True:
        adjacent = []
        curr_x = current_pos["x"]
        curr_y = current_pos["y"]
        curr_el = grid[curr_x][curr_y]["el"]
        visited.append({"x": curr_x, "y": curr_y})

        left_x, left_y = (curr_x - 1, curr_y)
        right_x, right_y = (curr_x + 1, curr_y)
        top_x, top_y = (curr_x, curr_y - 1)
        bottom_x, bottom_y = (curr_x, curr_y + 1)

        if left_x > -1:
            left_el = grid[left_x][left_y]["el"]
            left = {"x": left_x, "y": left_y,
                    "el": left_el, **grid[left_x][left_y]}
            el_diff = left["el"] - curr_el
            if not is_visited(left, visited) and el_diff <= 1:
                adjacent.append(left)

        if right_x < x_limit:
            right_el = grid[right_x][right_y]["el"]
            right = {"x": right_x, "y": right_y,
                     "el": right_el, **grid[right_x][right_y]}
            el_diff = right["el"] - curr_el
            if not is_visited(right, visited) and el_diff <= 1:
                adjacent.append(right)

        if top_y > -1:
            top_el = grid[top_x][top_y]["el"]
            top = {"x": top_x, "y": top_y, "el": top_el, **grid[top_x][top_y]}
            el_diff = top["el"] - curr_el
            if not is_visited(top, visited) and el_diff <= 1:
                adjacent.append(top)

        if bottom_y < y_limit:
            bottom_el = grid[bottom_x][bottom_y]["el"]
            bottom = {"x": bottom_x, "y": bottom_y,
                      "el": bottom_el, **grid[bottom_x][bottom_y]}
            el_diff = bottom["el"] - curr_el
            if not is_visited(bottom, visited) and el_diff <= 1:
                adjacent.append(bottom)

        steps += 1
        found_target = len(list(filter(
            lambda item: item["x"] == end["x"] and item["y"] == end["y"], adjacent))) > 0
        if found_target:
            break
        smallest_score = min(adjacent, key=lambda item: item["score"])
        print(smallest_score)
        current_pos = {"x": smallest_score["x"], "y": smallest_score["y"]}

    a_steps.append(steps)

print(min(a_steps))
