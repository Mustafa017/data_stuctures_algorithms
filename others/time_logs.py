import re


def parse1():
    for line in open('./logs.txt', 'r'):
        print(line.strip().split('[')[1].split(']')[0])


parse1()


def parse2():
    for line in open('./logs.txt', 'r'):
        print(" ".join(line.split()[3:5]).strip("[]"))


parse2()


def parse3():
    for line in open('./logs.txt'):
        print(re.split("\[|\]", line)[1])


parse3()
