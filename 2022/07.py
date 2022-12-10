from utils import read_file


dirs = [{"name": "/", "parent": "-", "size": 0}]

current_dir = {}
size_sum = 0
dir_depth = 0


def change_dir(d, i):
    global current_dir
    global size_sum
    global dir_depth

    if d == "/":
        current_dir['name'] = "/"
        current_dir['parent'] = "-"
        print(f"go to home directory")
        print(" ")
        return
    if d == "..":
        dir_depth -= 1
        print(
            f"change dir to level above, current dir is {current_dir['name']}")
        print(" ")
        try:
            current_dir_item = list(
                filter(lambda item: item["name"] == current_dir['name'] and item["parent"] == current_dir["parent"], dirs))[0]

            print(f"current dir item is {current_dir_item}")

            parent = list(
                filter(lambda item: item["name"] == current_dir_item["parent"], dirs))[0]

            print(f"parent item is: {parent}")

            current_dir_sum = current_dir_item["size"] + size_sum
            parent_dir_sum = parent["size"] + current_dir_sum

            print(f"parent {parent['name']} had total size {parent['size']}")

            for directory in dirs:
                directory.update(("size", current_dir_sum) for k, v in directory.items(
                ) if k == "name" and v == current_dir['name'])

            for directory in dirs:
                directory.update(("size", parent_dir_sum) for k, v in directory.items(
                ) if k == "name" and v == parent["name"])

            print(
                f"parent {parent['name']} now gets total size {parent['size']}")

            size_sum = 0
            current_dir['name'] = current_dir_item["parent"]
            current_dir['parent'] = parent["parent"]
            return

        except (IndexError, KeyError):
            print(f"current dir has no parent, in root dir /")
            current_dir['name'] = "/"
            current_dir['parent'] = "-"
            return

    else:
        dir_depth += 1
        current_dir_item = list(
            filter(lambda item: item["name"] == current_dir['name'] and item["parent"] == current_dir["parent"], dirs))[0]

        print(f"current is: {current_dir}")
        print(f"current dir item is {current_dir_item}")

        current_dir_sum = current_dir_item["size"] + size_sum

        print(f"total size for dir {current_dir['name']} is {current_dir_sum}")
        print(f"go to dir {i}-{d}")
        print(" ")

        for directory in dirs:
            directory.update(("size", current_dir_sum)
                             for k, v in directory.items() if k == "name" and v == current_dir["name"])
        size_sum = 0

        dirs.append(
            {"name": f"{i}-" + d, "parent": current_dir['name'], "size": 0})
        current_dir['parent'] = current_dir['name']
        current_dir['name'] = f"{i}-" + d


def is_int(s):
    try:
        return int(s)
    except ValueError:
        return False


total = 0

lines = read_file("input_7.txt")

for i, line in enumerate(list(lines)):
    split = line.split()
    cmd = split[1]
    size = split[0]

    if cmd == "cd":
        change_dir(split[2], i)
    if is_int(size):
        print(f"size info, adding {size}")
        size_sum += int(size)

for _ in range(dir_depth + 1):
    change_dir("..", _)

for d in dirs:
    print(d)
    print("")


under_limit = list(filter(lambda item: item["size"] <= 100000, dirs))


total = 0
for d in under_limit:
    # print("over limit")
    print(d)
    total += d["size"]

print(f"total size of folders less than limit: {total}")

# Part 2

print(f"total occupied space: {dirs[0]['size']}")
total_disk_space = 70000000
free_space = total_disk_space - dirs[0]['size']
print(f"free space {free_space}")
needed_space = 30000000 - free_space
print(f"needed space {needed_space}")

over_limit = list(filter(lambda item: item["size"] >= needed_space, dirs))
over_limit_sorted = sorted(over_limit, key=lambda d: d["size"])

print(
    f"size of smallest possible folder to delete: {over_limit_sorted[0]['size']}")
