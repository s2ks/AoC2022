#!/usr/bin/env python3

sums = []
sum = 0

while True:
    try:
        line = input()
        print(line)

        if line == "":
            sums.append(sum)
            sum = 0
        else:
            sum += int(line)
    except:
        break

sums.sort(reverse=True)
print(sums[0] + sums[1] + sums[2])
