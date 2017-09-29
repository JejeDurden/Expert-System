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
        for i in range(len(eq) - 1):
            char = eq[i]
            next_char = eq[i + 1]
            if i == 0 and is_op(char):
                print ("Error : Fact cannot start with operator.")
                sys.exit()
            if is_valid(char) is False or is_valid(next_char) is False:
                print ("Error : Some char are not valid.")
                sys.exit()
            elif is_op(char) and is_op(next_char):
                print ("Error : two operators cannot follow each other.")
                sys.exit()
            elif is_op(char) and (eq[i - 1] is '(' or next_char is ')'):
                print ("Error : bad placement of brackets or operand sign.")
                sys.exit()
            elif char.isalpha() and next_char.isalpha():
                print ("Error : two letters cannot follow each other.")
                sys.exit()
            elif char == next_char:
                print ("Error : two identical char cannot follow each other.")
                sys.exit()

def is_op(a):
    return (a is '+' or a is '^' or a is '|')

def is_valid(a):
    return ((a.isalpha() and a.isupper()) or is_valid_sign(a))

def is_valid_sign(a):
    return (a is '<' or a is '>' or a is '=' or a is '(' or a is ')' or a is '!' or is_op(a))
