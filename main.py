#!/usr/bin/python3

import sys
import os
import argparse
import re


def get_type(string):
    if not os.path.exists(string) or string[-4:] != '.txt':
        raise argparse.ArgumentTypeError("{0} is not a valid format or does not exist. Use --help for more informaion".format(string))
    return open(string, 'r')

def my_regex(data):
    line = data.read()
    line = re.sub('#[^>]\n', '', line)
    # lefteq = re.findall('.*[A-Z()!]\s*(?=\=>)|.*[A-Z()!]\s*(?=<\=>)', line.replace(' ', ''))
    # righteq = re.findall('(?=\=>).*[A-Z()!]\s*(?=\#)|(?=\<=>).*[A-Z()!]\s*(?=\#)', line.replace(' ', ''))
    eq = re.findall('.*[A-Z()!]\s*(?=\#)|.*[A-Z()!]\s*(?=\#)', line.replace(' ', ''))
    letters = re.findall('[A-Z]', line)
    print(letters)
    print(eq)
    letters = list(set(letters))
    letters.sort()
    print(letters)

def parse_arg(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=get_type, help="the file must be a .txt")
    args = parser.parse_args()
    return args.file

def main(argv):
    fd = parse_arg(argv)
    my_regex(fd)

if __name__ == "__main__":
    main(sys.argv[1:])
