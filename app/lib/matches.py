'''
Signs dictionary all possible signs are keys of this dictionary.
Array with three fields 1st is key sign, 2nd is sign that we could
get after get out match, the 3rd one for possible sign after putting
extra match and finally 4th value for changing position of a single match.
'''
from random import choice
from string import digits
from itertools import product, permutations

math_signs = '=+-'

#COORDINATES = [[0,0,0],[10,0,1],[110,0,0],[110,100,0],[10,200,1],[10,100,0],[0,100,1],[50,50,0],[40,0,1],[60,0,1]]

SIGNS2 = {}
SIGNS2['='] = [0]*8+[1]*2
SIGNS2['-'] = [0]*6+[1]+[0]*3
SIGNS2['+'] = [0]*6+[1]*2+[0]*2
SIGNS2['0'] = [1]*6+[0]*4
SIGNS2['1'] = [0]*2+[1]*2+[0]*6
SIGNS2['2'] = [0,1,1]*2+[1]+[0]*3
SIGNS2['3'] = [0]+[1]*4+[0,1]+[0]*3
SIGNS2['4'] = [1,0,1,1,0,0,1]+[0]*3
SIGNS2['5'] = [1,1,0]*2+[1]+[0]*3
SIGNS2['6'] = [1,1,0]+[1]*4+[0]*3
SIGNS2['7'] = [0]+[1]*3+[0]*6
SIGNS2['8'] = [1]*7+[0]*3
SIGNS2['9'] = [1]*5+[0,1]+[0]*3

SIGNS = {}
SIGNS['==']=[['=='],['-'],[],[]] 
SIGNS['=']=[['='],['-'],[],[]] 
SIGNS['-']=[['-'],[],['+','='],[]]
SIGNS['+']=[['+'],['-'],[],[]]
SIGNS['0']=[['0'],[],['8'],['6','9']]
SIGNS['1']=[['1'],[],['7']]
SIGNS['2']=[['2'],[],[],['3']]
SIGNS['3']=[['3'],[],['9'],['2','5'],]
SIGNS['4']=[['4'],[],[],[]]
SIGNS['5']=[['5'],[],['6','9'],['3']]
SIGNS['6']=[['6'],['5'],['8'],['0','9']]
SIGNS['7']=[['7'],['1'],[],[]]
SIGNS['8']=[['8'],['0','6','9'],[],[]]
SIGNS['9']=[['9'],['3','5'],['8'],['0','6']]
    
def new_check(e):
#    signs = [SIGNS2[i] for i in e]
    for i in range(10):
        if (e[3]=='=' and str(eval(e[:3]))==e[4]):
           return('true')

def check(f_digit, s_digit, t_digit, f_sign, s_sign,  equation):
    '''
    Check if current equation is correct
    '''
    try:
        for i in SIGNS[equation[0]][f_digit]:
            for j in SIGNS[equation[2]][s_digit]:
                for k in SIGNS[equation[4]][t_digit]:
                    for l in SIGNS[equation[1]][f_sign]:
                        for m in SIGNS[equation[3]][s_sign]:
                            if (m=='=' and ((l=='+' and int(i)+int(j)==int(k))
                                        or (l=='-' and int(i)-int(j)==int(k)))) \
                                        or (l=='=' and ((m=='+' and int(i)==int(j)+int(k)) \
                                        or (m=='-' and int(i)==int(j)-int(k)))) :
                                return i+l+j+m+k;
    except:
        return 0;


def solve(equation):
    '''
    Iterating throught all possibilities (brute force)
    '''
    for f_digit in range(4):
        for s_digit in range(4):
            for t_digit in range(4):
                for f_sign in range(3):
                    for s_sign in range(3):
                        if f_digit + f_sign + s_digit + s_sign + t_digit == 3 and 2 in [f_digit,s_digit,t_digit,f_sign,s_sign]:
                            result=check(f_digit, s_digit, t_digit, f_sign, s_sign,  equation)
                            if result:
                                return result
        
    return 0;

def solve2(equation):
    solution = []
    for j in set(permutations((0,0,0,1,2))) | set(permutations((0,0,0,0,3))):
        for k in product(*(SIGNS[equation[i]][j[i]] for i in range(5))):
            if(k.count("=")==1 and eval(''.join(k).replace('=','=='))):
                solution.append(''.join(k))
    return solution


ALL_EQUATIONS = [''.join(i) for i in product(digits,["+","-"],digits,["="],digits) if solve(''.join(i))]

