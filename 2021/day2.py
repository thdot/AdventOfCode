#! /usr/bin/env python3

commands = [ (c.split()[0], int(c.split()[1])) for c in open('inputs/day2.txt') ]

horizontal = depth = 0
for command, value in commands:
    if command == 'forward': horizontal += value
    if command == 'down':    depth += value
    if command == 'up':      depth -= value
print(horizontal * depth)

horizontal = depth = aim = 0
for command, value in commands:
    if command == 'forward':
        horizontal += value
        depth += aim * value
    if command == 'down':
        aim += value
    if command == 'up':
        aim -= value
print(horizontal * depth)
