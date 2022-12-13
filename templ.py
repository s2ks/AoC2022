#!/usr/bin/env python3

import sys

input = sys.stdin.read().rstrip()
lines = [line for line in input.split("\n")]

for line in lines:
    print(line)
