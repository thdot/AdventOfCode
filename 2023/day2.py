#! /usr/bin/env python3

import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
sum = 0
for l in open('inputs/day2.txt').readlines():
    idx, sets = re.match('Game (\d+): (.*)', l).groups()
    for s in sets.split(';'):
        d = {'red':0, 'green':0, 'blue':0}
        for cubes in s.split(','):
            n,color = re.match('\s*(\d+) (.*)', cubes).groups()
            d[color] += int(n)
        if d['red'] > MAX_RED or d['green'] > MAX_GREEN or d['blue'] > MAX_BLUE:
            break
    else:
        sum += int(idx)
print(sum)

sum = 0
for l in open('inputs/day2.txt').readlines():
    idx, sets = re.match('Game (\d+): (.*)', l).groups()
    d = {'red':0, 'green':0, 'blue':0}
    for s in sets.split(';'):
        for cubes in s.split(','):
            n,color = re.match('\s*(\d+) (.*)', cubes).groups()
            d[color] = max(d[color], int(n))
    sum += d['red'] * d['green'] * d['blue']
print(sum)
