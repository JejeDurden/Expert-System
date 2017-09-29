import re

def my_regex(data):
    line = data.read()
    line = re.sub('#(.+?)\n', '', line)
    print (line)
    # lefteq = re.findall('.*[A-Z()!]\s*(?=\=>)|.*[A-Z()!]\s*(?=<\=>)', line.replace(' ', ''))
    # righteq = re.findall('(?=\=>).*[A-Z()!]\s*(?=\#)|(?=\<=>).*[A-Z()!]\s*(?=\#)', line.replace(' ', ''))
    # print(lefteq)
    # print(righteq)
    eq = re.findall('.*[A-Z()!]\s*(?=\#)|.*[A-Z()!]\s*(?=\#)', line.replace(' ', ''))
    letters = re.findall('[A-Z]', line)
    letters.sort()
    true = re.findall('(?<=\n=).*' ,line)#ne doit pas etre en premiere ligne
    question = re.findall('(?<=\n\?).*' ,line)#ne doit pas etre en premiere ligne

    lists = [eq, letters, true, question]
    letters = list(set(letters))

    return lists
