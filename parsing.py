import os
import argparse
import sys

def parse_arg(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=open_file, help="the file must be a .txt")
    args = parser.parse_args()
    return args.file

def open_file(string):
    if not os.path.exists(string) or string[-4:] != '.txt':
        raise argparse.ArgumentTypeError("{0} is not a valid format or does not exist. Use --help for more informaion".format(string))
    return open(string, 'r')

def parse_eq(equations):
    for eq in equations:
        for char in eq:
            if is_op(char) and is_op(char - 1):
                print ("Error : two operators cannot follow each other.")
                sys.exit()
            if is_op(char) and (char - 1 is '(' or char + 1 is ')'):
                print ("Error : bad placement of brackets or {0}")
def is_op(a):
    return (a is '+' or a is '^' or a is '|')
