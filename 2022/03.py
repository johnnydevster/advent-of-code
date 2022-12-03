
from pathlib import Path

# Item priority
#
# Lowercase a-z: 1-26
# Uppercase A-Z: 27-52

alphabet = "abcdefghijklmnopqrstuvwxyz"

priorities = {}

for i, letter in enumerate(alphabet, start=1):
    priorities[letter] = i
    priorities[letter.upper()] = i + 26


def find_priority(letter):
    return priorities[letter]


p = Path(__file__).with_name("input.txt")


for row in file:
    print(row)


p = Path(__file__).with_name('input.txt')

with p.open('r') as f:
    lines = f.readlines()

    for line in lines:
