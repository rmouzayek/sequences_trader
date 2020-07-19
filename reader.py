import re 
import numpy as np



class Reader:
    def __init__(self, reader_input):
        self.input = reader_input if len(reader_input) > 1 else reader_input[0]
    
    def get_sequence(self):
        if type(self.input) == str:
            parsed = re.findall('-?\d+\.?\d*', self.input)
            return np.array(list(map(float, filter(None, parsed))))
        else:
            return np.array(self.input)
