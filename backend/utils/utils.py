
import numpy as np
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
            s += '-'
        s = s[0:-1]
        s += '|'
    s = s[0:-1]

    return s

def strToMat(s):
    mat = s.split('|')
    for i in range(len(mat)):
        mat[i] = [int(e) for e in mat[i].split('-')] #Shab mashalah

    return mat


def getNewVal(new_val_arr):

    new_val = ''

    for row in new_val_arr:
        value = 0

        for elem in row:
            value = (value << 1)
            if elem :
                value += 1

        new_val += np.base_repr(value,base=23)

    

    return new_val

        
    


        
        

