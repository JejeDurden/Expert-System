#!/usr/bin/python3

import sys
import argparse

def parse_arg(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("<file>", help="the file must be a .txt")
    args = parser.parse_args()

def main(argv):
    parse_arg(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
