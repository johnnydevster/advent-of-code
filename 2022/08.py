from utils import read_file
from collections import defaultdict

lines = read_file("input_8.txt")

cols = defaultdict(list)
rows = defaultdict(list)

for i, line in enumerate(list(lines), start=1):
    for i2, c in enumerate(line.strip("\n"), start=1):
        rows[i] = [*rows[i], int(c)]
        cols[i2] = [*cols[i2], int(c)]

new_cols = defaultdict(list)
new_rows = defaultdict(list)


def find_visibility(d, new_d):
    for key in d.keys():
        print(f"row {key}: {d[key]}")

        new_array = []
        for li, v in enumerate(d[key]):
            tag = v
            # start looking from left side
            #print(f"current value: {v}")
            left_side = d[key][:li]
            left_side_max_height = max(left_side, default=-1)

            right_side = d[key][li + 1:]
            right_side_max_height = max(right_side, default=-1)

            if v > left_side_max_height or v > right_side_max_height:
                tag = "x"

            new_array.append(tag)
        print(f"new array: {new_array}")
        new_d[key] = new_array


print("cols")
find_visibility(cols, new_cols)

print(" ")

print("rows")
find_visibility(rows, new_rows)

print(" ")
print(f"counting horizontally visible trees")

horizontal_count = 0

for key in new_rows.keys():
    trees = new_rows[key]
    print(f"row: {key}: {trees}")
    horizontal_count += trees.count("x")

print(" ")

vertical_count = 0

print(f"counting vertically visible trees")
for i, key in enumerate(cols.keys()):
    trees = new_cols[key]
    print(f"col: {key}: {trees}")
    for i2, tree in enumerate(trees, start=1):
        #print(f"current tree: {tree}")
        target_row = new_rows[i2]
        #print(f"target_row {target_row}")
        target_tree = target_row[i]

        if tree == "x" and target_tree != "x":
            vertical_count += 1
        #print(" ")

print(f"total visible trees: {horizontal_count + vertical_count}")
