#!/usr/bin/python3

import sys
import os
import argparse

def get_type(string):
    if not os.path.exists(string) or string[-4:] != '.txt':
        raise argparse.ArgumentTypeError("{0} is not a valid format or does not exist. Use --help for more informaion".format(string))
    return open(string, 'r')

def parse_arg(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=get_type, help="the file must be a .txt")
    args = parser.parse_args()
    return args.file

def main(argv):
    fd = parse_arg(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
