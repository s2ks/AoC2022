#!/usr/bin/env python3

p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0

while 1:
    try:
        x = input()
        l = len(x) // 2
        assert len(x[:l]) == len(x[l:]) and len(x[:l]) + len(x[l:]) == len(x)

        c1 = x[:l]
        c2 = x[l:]

        buf = []

        for c in c1:
            if c in c2 and c not in buf:
                buf.append(c)
                sum += p.index(c) + 1

    except EOFError:
        break

print(sum)
