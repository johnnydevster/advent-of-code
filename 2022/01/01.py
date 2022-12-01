with open('input.txt') as f:
    lines = f.readlines()

    values = []

    i = 1
    current_elf_sum = 0

    for line in lines:

        if line == "\n":

            values.append({"id": i, "sum": current_elf_sum})
            i += 1
            current_elf_sum = 0
            continue

        current_value = int(line.strip("\n"))
        current_elf_sum += current_value

    values.sort(key=lambda x: x["sum"], reverse=True)

    top_elf = values[0]

    top_three_elves = values[0:3]
    top_three_elves_sum = sum(elf["sum"] for elf in top_three_elves)

    print(top_three_elves_sum)
