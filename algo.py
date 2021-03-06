from parsing import parse_eq
from model import Equation

def create_eq(equations):
    parse_eq(equations)
    eq = []
    for string in equations:
        eq.append(Equation(string))
    return eq

def create_eq_graph_reverse(eq, letters):
    graph = {}
    for item in eq:
        graph[item] = []
        letter_right = get_letters(item.right)
        for leq in eq:
            letter_left = get_letters(leq.left)
            if not set(letter_left).isdisjoint(letter_right):
                graph[item].append(leq)
    return graph

def create_eq_graph(eq, letters):
    graph = {}
    for item in eq:
        graph[item] = []
        letter_left = get_letters(item.left)
        for leq in eq:
            child_right = get_letters(leq.right)
            if not set(child_right).isdisjoint(letter_left):
                graph[item].append(leq)
    return graph

def starting_points(eq, letters):
    for item in eq:
        missing = missing_values(item, letters)
        if not missing:
            item.status = True
    start_points = []
    for item in eq:
        if item.status is True:
            start_points.append(item)
    return start_points

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

def get_simple_answers(question, answer, letters):
    for q in question:
        for l in letters:
            if q == l.name:
                if l.status == True:
                    answer[q] = l.value
                    question.remove(q)
    return question, answer

def solve(equation, question):
    if equation.left[1] == '+':
        return(AND(equation.left[0], equation.left[2]))
    if equation.left[1] == '|':
        return(AND(equation.left[0], equation.left[2]))
    if equation.left[1] == '^':
        return (AND(equation.left[0], equation.left[2]))

def get_answers(graph, question, letters, i):
    for key, value in graph.items():
        for char in key.right:
            if char == question[i]:
                if key.status == True:
                    print(key.left)
                    answer = solve(key, question[i], letters)
                #backward_chaining(eq[l])
    return ({question[i]: True})

def ex_sys(graph, question, letters):
    answer = {}
    question, answer = get_simple_answers(question, answer, letters)
    for i in range(len(question)):
        answer.update(get_answers(graph, question, letters, i))
    print ()
