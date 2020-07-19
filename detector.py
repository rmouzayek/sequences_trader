from non_linear_polynomial_fit import Non_linear_polynomial_fit
from polynomial_fit import Polynomial_fit
from simple_signals import Simple_signals

class Detector: 
    def __init__(self, seq):
        self.seq = seq
        
    def __call__(self):
        Non_linear_polynomial_fit()(self.seq)
        Polynomial_fit()(self.seq)
        Simple_signals()(self.seq)
        
        