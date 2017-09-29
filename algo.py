from parsing import parse_eq
from model import Equation



def create_eq_graph(equations, letters):
    parse_eq(equations)
    eq = []
    for string in equations:
        eq.append(Equation(eq))
    for item in eq:
        missing = missing_values(item, letters)
        if not missing_values:
            item.status = True



def missing_values(eq, letters):
    list_missing_letter = []
    # print(eq)

    # for eqname in eq:
    #     print(eqname.name)

    # for char in letters:
    #     print(char.name)
    return list_missing_letter
