#!/usr/bin/python3

import sys
from parsing import parse_arg
from regex import my_regex
from model import Letter
from algo import create_eq_graph

def set_up(letters, true):
    for char in letters:
        for i in range(len(true[0])):
            if char.name is true[0][i]:
                char.status = True
                char.value = True

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
    start_points = starting_points(eq, letters)
    solve(graph, start_points)

if __name__ == "__main__":
    main(sys.argv[1:])
