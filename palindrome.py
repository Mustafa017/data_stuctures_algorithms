def check_solution1(s):
    return s == s[::-1]


def check_solution2(s):
    midpoint = len(s)//2
    for i in range(midpoint):
        if s[i] != s[-1-i]:
            return False
    return True


def check_solution3(s):
    midpoint = len(s)//2
    i = 0
    match = True
    while i < midpoint and match:
        if s[i] != s[-1-i]:
            match = False
        else:
            i += 1

    return match


print(check_solution1('racecar'))
print(check_solution2('malayalam'))
print(check_solution3('malayalam'))
