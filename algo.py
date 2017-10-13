from parsing import parse_eq
from model import Equation

def create_eq_graph(equations, letters):
    parse_eq(equations)
    eq = []
    for string in equations:
        eq.append(Equation(string))
    graph = {}
    for item in eq:
        graph[item] = []
        # print(item.name)
        letter_right = get_letters(item.right)
        for leq in eq:
            letter_left = get_letters(leq.left)
            if not set(letter_left).isdisjoint(letter_right):
                graph[item].append(leq)
        print(item)
        print("lol")
        for i in range(len(graph[item])):
            print(graph[item][i])
        print("coucou\n\n")
    return graph

def starting_points(equations, letters):
    parse_eq(equations)
    eq = []
    for string in equations:
        eq.append(Equation(string))
    for item in eq:
        missing = missing_values(item, letters)
        if not missing:
            item.status = True
    start_points = []
    for item in eq:
        if item.status is True:
            start_points.append(item)
            # print(item.name)

def get_letters(string):
    letters = []
    for i in range(len(string)):
        if string[i].isalpha():
            letters.append(string[i])
    return letters

def missing_values(eq, letters):
    list_missing_letter = []
    for i in range(len(eq.left)):
        if eq.name[i].isalpha():
            for letter in letters:
                if eq.name[i] is letter.name and letter.status is False:
                    list_missing_letter.append(letter)
    return list_missing_letter

def solve(graph, start_point):
    for item in graph:
        left_eq = Equation(item.name)
        #print(left_eq.get_left(item.name))
        #print(list(left_eq.get_left(item.name)))
        #print ("\n")
        # print(Equation(item.name))
    #print ("\n")
    #print (start_point)
    return 0

def read_equation(equations):
    pass
