import re

def my_regex(data):
    line = data.read()
    line = re.sub('#[^>]\n', '', line)
    # lefteq = re.findall('.*[A-Z()!]\s*(?=\=>)|.*[A-Z()!]\s*(?=<\=>)', line.replace(' ', ''))
    # righteq = re.findall('(?=\=>).*[A-Z()!]\s*(?=\#)|(?=\<=>).*[A-Z()!]\s*(?=\#)', line.replace(' ', ''))
    eq = re.findall('.*[A-Z()!]\s*(?=\#)|.*[A-Z()!]\s*(?=\#)', line.replace(' ', ''))
    letters = re.findall('[A-Z]', line)
    letters = list(set(letters))
    letters.sort()
    lists = [eq, letters]
    return lists
