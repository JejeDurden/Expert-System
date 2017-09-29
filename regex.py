import re

def my_regex(data):
    line = data.read()
    line = re.sub('#(.+?)\n', '\n', line)
    line = re.sub('\n+', '\n', line)
    print (line)
    # lefteq = re.findall('.*[A-Z()!]\s*(?=\=>)|.*[A-Z()!]\s*(?=<\=>)', line.replace(' ', ''))
    # righteq = re.findall('(?=\=>).*[A-Z()!]\s*(?=\#)|(?=\<=>).*[A-Z()!]\s*(?=\#)', line.replace(' ', ''))
    # print(lefteq)
    # print(righteq)
    eq = re.findall('.*[A-Z()!]\s*(?=\#)|.*[A-Z()!]\s*(?=\#)|.*[A-Z()!]\s*(?=\n)|.*[A-Z()!]\s*(?=\n)', line.replace(' ', ''))
    print(eq)
    letters = re.findall('[A-Z]', line)
    letters.sort()

    true = re.findall('(?<=\n=).*' ,line)#ne doit pas etre en premiere ligne
    print(true)
    question = re.findall('(?<=\n\?).*' ,line)#ne doit pas etre en premiere ligne
    print(question)

    lists = [eq, letters, true, question]
    letters = list(set(letters))

    return lists
