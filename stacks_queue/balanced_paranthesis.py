#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isBalanced(s):
    # Write your code here
    s_stack = []
    balanced = True
    o_par = '{[('
    c_par = '}])'
    for i in range(len(s)):
        if s[i] in '{[(':
            s_stack.append(s[i])
            # print(s_stack)
        else:
            # print(f'top={top} index={o_par.index(top)} arr={s_stack} symbol={s[i]}')
            if not s_stack:
                balanced = False
            else:
                top = s_stack.pop()
                if o_par.index(top) != c_par.index(s[i]):
                    balanced = False

    if balanced and not s_stack:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)

# smaple input
# 3
# {(([])[])[]}
# {(([])[])[]]}
# {(([])[])[]}[]

# sample output
# YES
# NO
# YES
