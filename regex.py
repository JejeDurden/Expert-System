import re

def my_regex(data):
    line = data.read()
    line = re.sub('#(.+?)\n', '\n', line)
    line = re.sub('\n+', '\n', line)
    # lefteq = re.findall('.*[A-Z()!]\s*(?=\=>)|.*[A-Z()!]\s*(?=<\=>)', line.replace(' ', ''))
    # righteq = re.findall('(?=\=>).*[A-Z()!]\s*(?=\#)|(?=\<=>).*[A-Z()!]\s*(?=\#)', line.replace(' ', ''))
    # eq = re.findall('.*[A-Z()!]\s*(?=\#)|.*[A-Z()!]\s*(?=\#)|.*[A-Z()!]\s*(?=\n)|.*[A-Z()!]\s*(?=\n)', line.replace(' ', ''))
    eq = re.findall('.*[A-Z()!]\s*(?=\=>).*[A-Z()!]|.*[A-Z()!]\s*(?=\<=>).*[A-Z()!]', line.replace(' ', ''))
    letters = re.findall('[A-Z]', line)
    true = re.findall('(?<=\n=).*' ,line)#ne doit pas etre en premiere ligne
    question = re.findall('(?<=\n\?).*' ,line)#ne doit pas etre en premiere ligne
    letters = list(set(letters))
    letters.sort()
    lists = [eq, letters, true, question]
    return lists
