import re

def parse1():
    with open('access.log', 'r') as f:
        for line in f:
            print(line.split()[1])


def parse2():
    with open('access.log', 'r') as f:
        for line in f:
            print(re.findall(r'\d{2}:\d{2}:\d{2}', line)[:1])

def parse3():
    with open('access.log', 'r') as f:
        for line in f:
            print(re.findall(r'\d:\d:\d', line)[0])

def parse4():
    with open('access.log', 'r') as f:
        print(f.split(' ')[1])

def parse5():
    with open('access.log', 'r') as f:
        for line in f:
            print(re.findall(r'\d+.\d+.\d+', line)[0])

print(parse1())
print(parse2())
#print(parse3())
#print(parse4())
#print(parse5())