import numpy as np 


from utils import _array_almost_equal, _correct_format



class Non_linear_polynomial_fit:   
    
    def non_linear_polynomial_fit(self, seq, factor):
        """ Un = a * Un-1 + b * factor**n + c
        """
        B = np.array(seq[1:4])
        A = np.array([[seq[k], factor ** (k + 1), 1] for k in range(3)])
        return np.around(np.linalg.solve(A,B), decimals=2)

    def non_linear_recursion(self, u, n, factor, coef):
        a, b, c = coef
        return a * u + b * (factor**n) + c

    def __call__(self, seq):
        Factor = {2,3,4}
        success = False
        for factor in Factor:
            try:
                coef = self.non_linear_polynomial_fit(seq, factor)
                Attempt = seq[:4]
                for n in range(4, len(seq)):
                    Attempt = np.append(Attempt, self.non_linear_recursion(Attempt[-1], n, factor, coef))
                if _array_almost_equal(Attempt, seq):
                    success = True
                    print('Non linear polynomial fit succeeded, factor = {}.\nUn = {} * Un-1 + {} * {}**n + {}.\nThe following term is {}.'.format(factor, _correct_format(coef[0]), _correct_format(coef[1]), factor, _correct_format(coef[2]), _correct_format(self.non_linear_recursion(seq[-1], (n+1), factor, coef))))
            except:
                pass
        if not success:
            print("No non linear polynomial fit\n")
            
            
            
        