from utils import read_file


lines = list(read_file("input_6.txt"))

chars = [char for char in lines[0]]

number_of_unique_markers = 14  # 4 for part 1.

count = number_of_unique_markers
old_list = chars[:number_of_unique_markers]

for char in chars[number_of_unique_markers:]:
    new_list = old_list[1:]
    new_list.append(char)
    print(f"old list: {old_list}")
    unique_sequence = True
    for i, c in enumerate(old_list):
        for i2, c2 in enumerate(old_list):
            if i == i2:
                continue
            if c == c2:
                print(f"char {c} is not unique, breaking...")
                unique_sequence = False
                break
        if not unique_sequence:
            old_list = new_list
            count += 1
            break
    if unique_sequence:
        print(f"sequence {old_list} seems to be unique")
        print(f"position is {count}")
        break
    print(" ")
