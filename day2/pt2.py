# A: rock       1
# B: paper      2
# C: scissors   3

# X: lose       0
# Y: draw       3
# Z: win        3

class Shape:
    def __init__(self, name, beats, draws, points):
        self.name = name
        self.beats = beats

shape = {
        "A": {"beats": "C", "points": 1, "draws": "A"},
        "B": {"beats": "A", "points": 2, "draws": "B"},
        "C": {"beats": "B", "points": 3, "draws": "C"},
        }

result = {
        "X": 0,
        "Y": 3,
        "Z": 6,
        }


total = 0

while 1:
    try:
        x = input().split()

        you = x[0]
        res = x[1]

        points = result[res]

        turn = ""

        if points == 6:
            # need to win so pick whichever is not in the dict
            for key in shape:
                if key != shape[you]["beats"] and key != shape[you]["draws"]:
                    turn = key

        elif points == 3:
            #need to draw
            turn = shape[you]["draws"]
        else:
            #need to lose
            turn = shape[you]["beats"]

        points += shape[turn]["points"]

        # print(points)

        print(f"{x} {points} {turn}")

        total += points
    except:
        break

print(total)
