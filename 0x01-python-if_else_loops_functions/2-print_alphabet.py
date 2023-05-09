#!/usr/bin/python3

for c in range(ord('a'), ord('z') + 1):
    print("{:c}".format(c), end='' if chr(c) != 'z' else '\n')
