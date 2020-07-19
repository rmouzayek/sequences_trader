import numpy as np 


from utils import _array_almost_equal, _correct_format



class Polynomial_fit:   
    
    def polynomial_fit(self, seq):
        """ Un = a * Un-1 + b * n + c
        """
        B = np.array(seq[1:4])
        A = np.array([[seq[k], k + 1, 1] for k in range(3)])
        return np.around(np.linalg.solve(A,B), decimals=2)
     
    def recursion(self, u, n, coef):
        a, b, c = coef
        return a * u + b * n + c
    
    def __call__(self, seq):
        try:
            coef = self.polynomial_fit(seq)
            Attempt = seq[:4]
            for n in range(4, len(seq)):
                Attempt = np.append(Attempt, self.recursion(Attempt[-1], n, coef))
            if _array_almost_equal(Attempt, seq):
                print('Polynomial fit succeeded.\nUn = {} * Un-1 + {} * n + {}.\nThe following term is {}.\n'.format(_correct_format(coef[0]), _correct_format(coef[1]), _correct_format(coef[2]), _correct_format(self.recursion(seq[-1], (n+1), coef))))
            else: 
                print("No polynomial fit\n")
        except:
            print("No polynomial fit\n")