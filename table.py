import pandas as pd 
from IPython.core.display import display, HTML
import inspect


from utils import _correct_format
from functions import Functions



class Table:
    def __init__(self, sequence, functions, name):
        self.functions = functions
        self.sequence = sequence
        self.name = name
        
        columns = [_correct_format(str(item)) for item in self.sequence] + ['initial serie']
        self.dataframe = pd.DataFrame(self._get_data(), columns = columns)
        
    def _get_data(self):
        All_lines = []
        attrs = (getattr(self.functions, name) for name in Functions.__dict__)
        methods = list(filter(inspect.ismethod, attrs))
        for method in methods:
            try:
                output = method(self.sequence)
                if isinstance(output, list):
                    All_lines += output
                else:
                    All_lines += [output]
            except TypeError as err:
                print(err)
        return [line.get() for line in All_lines]
    
    def display(self):
        table = self.dataframe.astype('str')
        table = table.applymap(_correct_format)
        print('---------------------------------------')
        print('{} :\n'.format(self.name))
        display(HTML(table.to_html(index=False, col_space=100)))