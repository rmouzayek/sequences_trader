import numpy as np



def _convert_to_array(variable):
        if variable == None:
            return None
        elif type(variable) == str: 
            variable = [variable]
        return np.array(variable)
    
def _correct_format(string):
    string = str(string)
    try:
        if float(string) == 0:
            return '0'
    except:
        pass
    while (string[-1] == '0' or string[-1] == '.') and '.' in string:
        string = string[:-1]
    return string

def _sum_digits(nbr):
    return np.sum(list(map(float, [digit for digit in str(nbr) if digit not in {'.', '-'}])))

def _factorials(size):
    return np.array([np.math.factorial(n + 1) for n in range(size)])

def _prime_nbrs(size):
    Prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    return np.array(Prime[:size])

def _hide_numpy_warnings():
    np.seterr(all='ignore')
    
def _array_almost_equal(A,B):
    return np.sum(np.around(np.array(A) - np.array(B), decimals = 2)) == 0

def _array_almost_same_element(array):
    return _array_almost_equal(array, np.repeat(array[0], len(array)))