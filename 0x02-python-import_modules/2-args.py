#!/usr/bin/python3

import sys

argc = len(sys.argv) - 1
plural_suffix = 's' if argc != 1 else ''

print("{} arguments".format(argc), end='')
if argc == 0:
    print('.')
else:
    print(':', end='\n')
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
