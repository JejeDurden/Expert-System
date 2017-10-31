#!/usr/bin/python3

import sys
from parsing import parse_arg
from regex import my_regex
from model import Letter, Equation
from algo import create_eq_graph_reverse, create_eq_graph, starting_points, ex_sys, create_eq

def set_up_letters(letters, true):
    for char in letters:
        for i in range(len(true[0])):
            if char.name is true[0][i]:
                char.status = True
                char.value = True
    return letters

def set_up_eq(eq, letters):
    prev = ""
    for i in range(len(eq)):
        eq[i].left = list(eq[i].left)
        for k in range(len(eq[i].left)):
            for l in letters:
                if l.name == eq[i].left[k]:
                    if l.status == True:
                        if eq[i].left[k - 1] == '!':
                            eq[i].left[k] = not l.value
                        else:
                            eq[i].left[k] = l.value
    for i in range(len(eq)):
        if '!' in eq[i].left:
            eq[i].left.remove('!')
    return eq

def main(argv):
    fd = parse_arg(argv)
    lists = my_regex(fd)
    letters = []
    eq = lists[0]
    for letter in lists[1]:
        letters.append(Letter(letter))
    true = lists[2]
    question = list(''.join(lists[3]))
    question.remove(' ')
    lists.clear()
    letters = set_up_letters(letters, true)
    eq = create_eq(eq)
    graph_reverse = create_eq_graph_reverse(eq, letters)
    graph = create_eq_graph(eq, letters)
    start_points = starting_points(eq, letters)
    eq = set_up_eq(eq, letters)
    ex_sys(graph, question, letters)

if __name__ == "__main__":
    main(sys.argv[1:])
