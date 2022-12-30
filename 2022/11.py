from utils import read_file
from math import prod


lines = read_file("input_11_test.txt")

monkeys = {}

monkey = ""
items = []
operation = ""
test_divisor = 0
test_true = ""
test_false = ""
test = ""


def create_op_function(op, value):
    global operation

    def func(old_val):
        new_val = 0
        if value == "old":
            new_val = old_val
        else:
            new_val = int(value)
        if op == "+":
            return old_val + new_val
        if op == "*":
            return old_val * new_val

    operation = func


def create_test_function(test_divisor, test_true, test_false):
    global test

    def func(val):
        if val % test_divisor == 0:
            return test_true
        else:
            return test_false
    test = func


def add_to_end(values, value):
    yield from values
    yield value


for line in lines:
    split = line.strip().split(" ")

    if split[0] == "Monkey":
        monkey = f"Monkey-{split[1][:-1]}"
    if split[0] == "Starting":
        items = (int(i.strip(",")) for i in split[2:])
    if split[0] == "Operation:":
        create_op_function(*split[-2:])
    if split[0] == "Test:":
        test_divisor = int(split[-1])
    if split[0] == "If":
        if split[1] == "true:":
            test_true = f"Monkey-{split[-1]}"
        if split[1] == "false:":
            test_false = f"Monkey-{split[-1]}"
            create_test_function(test_divisor, test_true, test_false)

            monkeys[monkey] = {
                "items": items,
                "inspects": 0,
                "operation": operation,
                "test": test,
            }


for i in range(0, 100):
    for monkey in monkeys.keys():
        curr = monkeys[monkey]

        for item in curr["items"]:
            print(item)
            print(" ")
            level = curr["operation"](item)
            target_monkey = curr["test"](level)

            monkeys[target_monkey]["items"] = add_to_end(
                monkeys[target_monkey]["items"], level)
            curr["inspects"] += 1


print(" ")

inspects = []
for monkey in monkeys.keys():
    inspects.append(monkeys[monkey]["inspects"])
print(inspects)

print(f"Part 1: {prod(sorted(inspects)[-2:])}")
