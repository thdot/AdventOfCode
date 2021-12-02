#! /usr/bin/env python3

depths = [ int(d) for d in open('input') ]

print(sum( [ d1 < d2 for d1,d2 in zip(depths, depths[1:]) ]))

print(sum( [d1+d2+d3 < d2+d3+d4 for d1,d2,d3,d4 in zip(depths, depths[1:], depths[2:], depths[3:]) ]))

