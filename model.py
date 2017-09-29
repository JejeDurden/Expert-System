class Letter:
    def __init__(self, name):
        self.status = False
        self.value = False
        self.conn = {}
        self.name = name

class Equation:
    def __init__(self, name):
        self.status = False
        self.left = get_left(name)
        self.right = get_right(name)
        self.name = name

    def get_left(name):
        for i in range(len(name)):
            if name[i] is '<' or name[i] is '=':
                return (name[:i])

    def get_right(name):
        for i in range(len(name)):
            if name[i] is '>':
                return (name[i:])
