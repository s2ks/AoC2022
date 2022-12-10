#!/usr/bin/env python3

greatest = 0
sum = 0

while True:
    try:
        line = input()
        print(line)

        if line == "":
            greatest = sum if sum > greatest else greatest
            sum = 0
        else:
            sum += int(line)

    except:
        break

print(greatest)
