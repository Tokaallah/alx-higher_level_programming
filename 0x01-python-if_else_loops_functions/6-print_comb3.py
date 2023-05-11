#!/usr/bin/python3

for i in range(10):
    for j in range(i+1, 10):
        for k in range(j+1, 10):
            print("{:d}{:d}{:d}".format(i, j, k), end='')
            if i < 7 or (i == 7 and j < 8) or (i == 8 and j == 8 and k < 9):
                print(", ", end='')
            else:
                print()
