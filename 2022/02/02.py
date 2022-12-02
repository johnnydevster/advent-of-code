from pathlib import Path

# SCORING
#
# Shape Points:
#
#   Rock:      1
#   Paper:     2
#   Scissors:  3
#
# Round Points:
#
#   Loss:      0
#   Draw:      3
#   Win:       6

# DEFINITIONS
#
# Opponents:
#   A: Rock
#   B: Paper
#   C: Scissors
#
# Player:
#   X: Rock
#   Y: Paper
#   Z: Scissors

win_conditions = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

loss_conditions = {value: key for (key, value) in win_conditions.items()}

worths = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}


class PlayHand:
    def __init__(self, type):
        self.type = type
        self.worth = worths[type]
        self.wins_against = win_conditions[type]
        self.loses_against = loss_conditions[type]

    def __str__(self):
        return f"PlayHand({self.type}, worth: {self.worth})"

    def play(self, hand):
        if hand.wins_against == self.type:
            # The played hand wins
            return 6 + hand.worth
        if hand.type == self.type:
            # Same type, it's a tie
            return 3 + hand.worth
        # Only loss condition left
        return hand.worth


rock = PlayHand("rock")
paper = PlayHand("paper")
scissors = PlayHand("scissors")

# Part 1

opponent_defs = {
    "A": rock,
    "B": paper,
    "C": scissors,
}

player_defs = {
    "X": rock,
    "Y": paper,
    "Z": scissors
}

score = 0

p = Path(__file__).with_name('input.txt')

with p.open('r') as f:
    lines = f.readlines()

    for line in lines:
        opponent_hand = opponent_defs[line[0]]
        player_hand = player_defs[line[2]]
        points = opponent_hand.play(player_hand)
        score += points

print(f"Part 1 solution: {score}")

# Part 2

round_strategy = {
    "X": "lose",
    "Y": "tie",
    "Z": "win"
}

score = 0

with p.open('r') as f:
    lines = f.readlines()

    for line in lines:
        opponent_hand = opponent_defs[line[0]]
        strategy = round_strategy[line[2]]

        if strategy == "lose":
            player_hand = PlayHand(opponent_hand.wins_against)
            score += opponent_hand.play(player_hand)
        if strategy == "tie":
            score += opponent_hand.play(opponent_hand)
        if strategy == "win":
            player_hand = PlayHand(opponent_hand.loses_against)
            score += opponent_hand.play(player_hand)

print(f"Part 2 solution: {score}")
