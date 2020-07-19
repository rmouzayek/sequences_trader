import numpy as np


from utils import _convert_to_array



class Line: 
    def __init__(self, sequence, label, prefix=None, suffix=None):
        self.sequence = sequence
        self.label = _convert_to_array(label)
        self.prefix = _convert_to_array(prefix) 
        self.suffix = _convert_to_array(suffix) 
    

    def get(self):
        line = np.hstack((self.prefix, self.sequence, self.suffix, self.label))
        return line[line != None]