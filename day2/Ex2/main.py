from enum import Enum

class Shape(Enum):
    X = 1
    Y = 2
    Z = 3

class Outcome(Enum):
    LOST = 0
    DRAW = 3
    WON = 6

def contest(round):
    sum = 0
    match round[0]:
        case 'A':
            if round[1] == "X":
                # lost
                sum += Shape['Z'].value + Outcome['LOST'].value
            if round[1] == "Y":
                # draw
                sum += Shape['X'].value + Outcome['DRAW'].value
            if round[1] == "Z":
                # won
                sum += Shape['Y'].value + Outcome['WON'].value
        case 'B':
            if round[1] == "X":
                # lost
                sum += Shape['X'].value + Outcome['LOST'].value
            if round[1] == "Y":
                # draw
                sum += Shape['Y'].value + Outcome['DRAW'].value
            if round[1] == "Z":
                # won
                sum += Shape['Z'].value + Outcome['WON'].value
        case 'C':
            if round[1] == "X":
                # lost
                sum += Shape['Y'].value + Outcome['LOST'].value
            if round[1] == "Y":
                # draw
                sum += Shape['Z'].value + Outcome['DRAW'].value
            if round[1] == "Z":
                # won
                sum += Shape['X'].value + Outcome['WON'].value
    return sum

f = open("day2/tournament.txt", "r")
f = f.read()

rounds = []

for round in f.split("\n"):
    rounds.append(round.split())

sum = 0
for round in rounds:
    sum += contest(round)
print(sum)