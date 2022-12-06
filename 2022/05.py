from utils import read_file

stack = {
    "1": ["R", "P", "C", "D", "B", "G"],
    "2": ["H", "V", "G"],
    "3": ["N", "S", "Q", "D", "J", "P", "M"],
    "4": ["P", "S", "L", "G", "D", "C", "N", "M"],
    "5": ["J", "B", "N", "C", "P", "F", "L", "S"],
    "6": ["Q", "B", "D", "Z", "V", "G", "T", "S"],
    "7": ["B", "Z", "M", "H", "F", "T", "Q"],
    "8": ["C", "M", "D", "B", "F"],
    "9": ["F", "C", "Q", "G"]
}


lines = read_file("input_5.txt")

for line in list(lines)[10:]:
    split = line.split(" ")

    quant = int(split[1])

    from_pos = split[3]
    to_pos = split[5].strip("\n")

    print(f"quant {quant}")
    print(f"from {from_pos}")
    print(f"to {to_pos}")

    print(" ")

    from_pos_stack_length = len(stack[from_pos])

    # Lift up (copy) the boxes that should be moved, (and reverse them, for part 1)
    moved_boxes = list(
        stack[from_pos][from_pos_stack_length - quant:])

    # Remove these boxes from the old stack
    stack[from_pos] = stack[from_pos][:-quant]

    # Add the lifted boxes to the end of the new stack
    stack[to_pos].extend(moved_boxes)

    print(f"moved boxes: {moved_boxes}")
    print(f"old box stack: {stack[from_pos]}")
    print(f"new box stack: {stack[to_pos]}")
    print(" ")

keys = dict.keys(stack)

for key in keys:
    print(f"Stack {key} top: {stack[key][-1]}")
