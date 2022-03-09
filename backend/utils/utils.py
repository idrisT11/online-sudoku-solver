

import random


def generateToken():
    token = ""
    for i in range(32):
        val = random.randint(0, 15)
        token += hex(val)[2:]

    token = token.upper()
    return token

def matToStr(mat):
    s = ''

    for row in mat:
        for elem in row:
            s += str(elem)
            s += '+'
        s = s[0:-2]
        s += '#'
    s = s[0:-2]

    return s
        
        

