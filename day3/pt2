#!/usr/bin/env python3

p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0

while 1:
    try:
        x1 = input()
        x2 = input()
        x3 = input()

        buf = []

        for c in x1:
            if c in x2 and c in x3 and c not in buf:
                buf.append(c)
                sum += p.index(c) + 1

    except EOFError:
        break

print(sum)
