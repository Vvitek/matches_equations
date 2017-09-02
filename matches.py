'''
Signs dictionary all possible signs are keys of this dictionary.
Array with three fields 1st is key sign, 2nd is sign that we could
get after get out match, the 3rd one for possible sign after putting
extra match and finally 4th value for changing position of a single match.
'''
from random import choice
from string import digits
from itertools import product

math_signs = '=+-'

SINGNS = {}
SINGNS['=']=[['='],['-'],[]] 
SINGNS['-']=[['-'],[],['+','=']]
SINGNS['+']=[['+'],['-'],[]]
SINGNS['0']=[['0'],[],['8'],['6','9']]
SINGNS['1']=[['1'],[],['7']]
SINGNS['2']=[['2'],[],[],['3']]
SINGNS['3']=[['3'],[],['9'],['2','5'],]
SINGNS['4']=[['4'],[],[],[]]
SINGNS['5']=[['5'],[],['6','9'],['3']]
SINGNS['6']=[['6'],['5'],['8'],['0','9']]
SINGNS['7']=[['7'],['1'],[],[]]
SINGNS['8']=[['8'],['0','6','9'],[],[]]
SINGNS['9']=[['9'],['3','5'],['8'],['0','6']]
    
def check(f_digit, s_digit, t_digit, f_sign, s_sign,  equation):
    '''
    Check if current equation is correct
    '''
    try:
        for i in SINGNS[equation[0]][f_digit]:
            for j in SINGNS[equation[2]][s_digit]:
                for k in SINGNS[equation[4]][t_digit]:
                    for l in SINGNS[equation[1]][f_sign]:
                        for m in SINGNS[equation[3]][s_sign]:
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
                        if f_digit + f_sign + s_digit + s_sign + t_digit == 3:
                            result=check(f_digit, s_digit, t_digit, f_sign, s_sign,  equation)
                            if result:
                                return result
        
    return 0;

ALL_EQUATIONS = [''.join(i) for i in product(digits,["+","-"],digits,["="],digits) if solve(''.join(i))]

if __name__ == '__main__':
    generate_equations()
