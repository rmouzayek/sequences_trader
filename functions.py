import numpy as np


from utils import _sum_digits, _factorials, _prime_nbrs
from line import Line



class Functions: 
    def diff(self, seq):
        return Line(np.around(seq[1:] - seq[:-1], decimals=2), 'difference element wise', ['-'])

    def diff_of_diff(self, seq):
        diff = seq[1:] - seq[:-1]
        return Line(np.around(diff[1:] - diff[:-1], decimals=2), 'difference of difference element wise', ['-', '-'])
    
    def cum_sum(self, seq):
        return Line(np.cumsum(seq), 'cumulative sum')
    
    def ratio(self, seq): 
        return Line(np.around(seq[1:] / seq[:-1], decimals=2), 'factor to previous element', ['-'])

    def normalized_diff(self, seq):
        indexes = np.array(range(1, len(seq)))
        return Line(np.around((seq[1:] - seq[:-1]) / indexes, decimals=2), 'Un - Un-1 / n', ['-'])

    def normalized_log(self, seq):
        indexes = np.array(range(1, len(seq)))
        return Line(np.around(np.log(seq[1:] - seq[:-1]) / indexes, decimals=2), 'log(Un - Un-1) / n', ['-'])

    def ratio_u0(self, seq):
        indexes = np.array(range(1, len(seq) + 1))
        return Line(np.around(seq / seq[0]/ indexes, decimals=2), 'Un / U0') 

    def multiple(self, seq):
        return [Line(np.round(seq * nbr, 2), 'sequence multiplied by {}'.format(nbr)) for nbr in range(2, 7)]

    def diff_multiple(self, seq): 
        return [Line(np.round((seq * nbr)[1:] - (seq * nbr)[:-1] , 2), 'difference between term for the sequence times {}'.format(nbr), ['-']) for nbr in range(2, 6)]

    def sum_digits(self, seq):
        return Line(np.vectorize(_sum_digits)(seq), 'sum of the digits')

    def factorial(self, seq):
        return Line(_factorials(len(seq)), 'factorials')

    def prime_nbrs(self, seq):
        return Line(_prime_nbrs(len(seq)), 'Prime numbers')
