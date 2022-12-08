from utils import read_file

lines = read_file("input_7_test.txt")


commands = {
    "ls": "ls"
}

dirs = [
    {"name": "/", "size": 0, "contains": [
        {"name": "b", "size": 0, "contains": [
            {"name": "e", "size": 0, "contains": [
                {"name": "f", "size": 500}
            ]},
            {"name": "g", "size": 100},
            {"name": "h", "size": 200},
        ]},
        {"name": "c", "size": 200}
    ]}
]

dirs_two = [
    {"name": "a", "size": 0},
    {"name": "b", "parent": "a", "size": 0},
    {"name": "c", "parent": "b", "size": 500},
    {"name": "d", "parent": "b", "size": 200},
    {"name": "e", "parent": "b", "size": 300},
    {"name": "f", "parent": "a", "size": 300},
]

size_count = 0
curr_file = ""

for file in dirs_two:
    name = file["name"]


def traverse(arr):
    size = 0

    for file in arr:
        print(f'Name: {file["name"]}, size: {file["size"]}')
        curr_file = file["name"]
        size += file["size"]

        if "contains" in file:
            print(f'{file["name"]} is a directory, run traverse() again')
            traverse(file["contains"])
            break
    print(f"{file['name']} size is {size}")
    print("done")
    print(" ")


def change_dir(d):
    if d == "/":
        print(f"go to home directory")
    if d == "..":
        print(f"go to dir above")


def list_current_directory():
    print("directory contents: ")


def run_command(cmd, arg):
    print(cmd)
    if cmd == "cd":
        change_dir(arg)
    if cmd == "ls":
        list_current_directory()


for line in lines:
    split = line.split()

    current_dir = split[1]
    dir_size = 0

    if split[0] == 'cd' and split[1] != "..":
        print(split[1:])
