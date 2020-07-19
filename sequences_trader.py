import re 
import numpy as np
import pandas as pd 
import inspect
from IPython.core.display import display, HTML


from utils import _convert_to_array, _sum_digits, _factorials, _prime_nbrs, _correct_format, _hide_numpy_warnings


class Reader:
    def __init__(self, *reader_input):
        self.input = reader_input if len(reader_input) > 1 else reader_input[0]
    
    def get_sequence(self):
        if type(self.input) == str:
            parsed = re.findall('-?\d+\.?\d*', self.input)
            return np.array(list(map(float, filter(None, parsed))))
        else:
            return np.array(self.input)

class Line: 
    def __init__(self, sequence, label, prefix=None, suffix=None):
        self.sequence = sequence
        self.label = _convert_to_array(label)
        self.prefix = _convert_to_array(prefix) 
        self.suffix = _convert_to_array(suffix) 
    

    def get(self):
        line = np.hstack((self.prefix, self.sequence, self.suffix, self.label))
        return line[line != None]
        

class Functions: 
    def __init__(self):
    
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


class Table:
    def __init__(self, functions):
        self.functions = functions
        self.sequence = functions.seq
        
        columns = [_correct_format(str(item)) for item in self.sequence] + ['initial serie']
        self.dataframe = pd.DataFrame(self._get_data(), columns = columns)
        
    def _get_data(self):
        All_lines = []
        #attrs = (getattr(self.functions, name) for name in dir(self.functions) if name != '__init__')
        attrs = (getattr(self.functions, name) for name in Functions.__dict__ if name != '__init__')
        methods = list(filter(inspect.ismethod, attrs))
        for method in methods:
            try:
                output = method()
                if isinstance(output, list):
                    All_lines += method()
                else:
                    All_lines += [method()]
            except TypeError as err:
                print(err)
        return [line.get() for line in All_lines]
    
    def display(self):
        table = self.dataframe.astype('str')
        table = table.applymap(_correct_format)
        display(HTML(table.to_html(index=False, col_space=100)))
        
    
if __name__ == '__main__':
    _hide_numpy_warnings()
    s = Reader([54, 54, 3, 6 ,8]).get_sequence()
    f = Functions(s)
    t = Table(f)
    t.display()
    #seq = r.get_sequence()
    #print(sum_digits(seq).get())
       