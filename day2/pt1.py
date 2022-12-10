

# A: rock       1
# B: paper      2
# C: scissors   3

# X: rock       1
# Y: paper      2
# Z: scissors   3

class Shape:
    def __init__(self, name, beats, draws, points):
        self.name = name
        self.beats = beats

shape = {
        "X": {"beats": "C", "points": 1, "draws": "A"},
        "Y": {"beats": "A", "points": 2, "draws": "B"},
        "Z": {"beats": "B", "points": 3, "draws": "C"},
        }


total = 0

while 1:
    try:
        x = input().split()

        me = x[1]
        you = x[0]

        beats = you == shape[me]["beats"]
        draws = you == shape[me]["draws"]
        points = shape[me]["points"]
        points += 3 if not beats and draws else 0
        points += 6 if beats else 0

        # print(points)

        print(f"{x} {points}")

        total += points
    except:
        break

print(total)
