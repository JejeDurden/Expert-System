#!/usr/bin/python3

import sys
from parsing import parse_arg
from regex import my_regex

def main(argv):
    fd = parse_arg(argv)
    lists = my_regex(fd)
    

if __name__ == "__main__":
    main(sys.argv[1:])
