#!/usr/local/bin/python3

import sys

number = sys.argv[1]
base = 10

if sys.argv.__len__() == 3:
	base = int(sys.argv[2])

if number.startswith('0x'):
	base = 16

if number.startswith('0b') and base == 10:
	base = 2

x = int(number, base)

print('base 2:  ', bin(x))
print('base 8:  ', oct(x))
print('base 10: ', x)
print('base 16: ', hex(x))