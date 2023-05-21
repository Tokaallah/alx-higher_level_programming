#!/usr/bin/python3

for char_code in range(90, 64, -1):
    print(chr(char_code), end='')
    char_code =+ 6
    print(chr(char_code), end='')
