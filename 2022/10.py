from utils import read_file

lines = read_file("input_10.txt")

cycle = 0
values = {}

x = 1

for line in lines:
    commands = line.strip("\n").split(" ")

    if commands[0] == "noop":
        cycle += 1
        values[cycle] = x
    else:
        for i in range(0, 2):
            cycle += 1
            values[cycle] = x
        x += int(commands[1])

signal_stops = [
    20, 60, 100, 140, 180, 220
]

signal_values = []

for signal in signal_stops:
    signal_values.append(signal * values[signal])

print(f"Part 1: {sum(signal_values)}")
