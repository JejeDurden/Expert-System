from parsing import parse_eq

def create_eq_graph(equations, letters):
    parse_eq(equations)
    eq = []
    for string in equations:
        eq.append(Equation(eq))
    for item in eq:
        missing = missing_values(item, letters):
        if missing_values.isempty():
            item.status = True

def missing_values(eq, letters):
