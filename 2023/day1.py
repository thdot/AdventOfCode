#! /usr/bin/env python3

import re

s = 0
for l in open('inputs/day1.txt').readlines():
    l = re.sub('[a-z]', '', l[:-1])
    s += int(l[0] + l[-1])
print(s)

NR = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
s = 0
for l in open('inputs/day1.txt').readlines():
    l = l[:-1]
    l = re.sub('|'.join(['(?=(%s))' % e for e in NR]),
            lambda m: str(NR.index([e for e in m.groups() if e][0]) + 1), l)
    l = re.sub('[a-z]', '', l)
    s += int(l[0] + l[-1])
print(s)
