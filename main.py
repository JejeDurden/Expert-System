#!/usr/bin/python3

import sys
from parsing import parse_arg
from regex import my_regex
from model import Letter

def main(argv):
    fd = parse_arg(argv)
    lists = my_regex(fd)
    letters = []
    eq = lists[0]
    for letter in lists[1]:
        letters.append(Letter(letter))
    true = lists[2]
    question = lists[3]
    lists.clear()
    set_up(letters, true)
    graph = create_eq_graph(eq, letters)




if __name__ == "__main__":
    main(sys.argv[1:])
