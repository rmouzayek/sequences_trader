from utils import _array_almost_same_element, _correct_format
from functions import Functions



class Simple_signals: 
    
    def __call__(self, seq):
        self.seq = seq 
        self.seq_alt_1 = seq[::2]
        self.seq_alt_2 = seq[1::2]
        self.functions = Functions()
        
        self.detect_ratio_signal()
        self.detect_diff_signal()

    def detect_ratio_signal(self):
        seq_ratio = self.functions.ratio(self.seq).sequence
        if _array_almost_same_element(seq_ratio):
            print("Strong signal of a ratio {}. Next term is {}.".format(_correct_format(seq_ratio[0]), _correct_format(self.seq[-1] * seq_ratio[0])))
        else:
            seq_ratio_alt_1 = self.functions.ratio(self.seq_alt_1).sequence
            seq_ratio_alt_2 = self.functions.ratio(self.seq_alt_2).sequence
            if _array_almost_same_element(seq_ratio_alt_1) and len(self.seq_alt_1) > 2:
                print("Signal of a ratio {} for list alternating 1. Next term is {}.".format(_correct_format(seq_ratio_alt_1[0]), _correct_format(self.seq_alt_1[-1] * seq_ratio_alt_1[0])))
            if _array_almost_same_element(seq_ratio_alt_2) and len(self.seq_alt_2) > 2:
                print("Signal of a ratio {} for list alternating 2. Next term is {}.".format(_correct_format(seq_ratio_alt_2[0]), _correct_format(self.seq_alt_2[-1] * seq_ratio_alt_2[0])))

    def detect_diff_signal(self):
        seq_diff = self.functions.diff(self.seq).sequence
        if _array_almost_same_element(seq_diff):
            print("Strong signal of a diff {}. Next term is {}.".format(_correct_format(seq_diff[0]), _correct_format(self.seq[-1] + seq_diff[0])))
        else:
            seq_diff_alt_1 = self.functions.diff(self.seq_alt_1).sequence
            seq_diff_alt_2 = self.functions.diff(self.seq_alt_2).sequence
            if _array_almost_same_element(seq_diff_alt_1) and len(self.seq_alt_1) > 2:
                 print("Signal of a diff {} for list  alternating 1. Next term is {}.".format(_correct_format(seq_diff_alt_1[0]), _correct_format(self.seq_alt_1[-1] + seq_diff_alt_1[0])))
            if _array_almost_same_element(seq_diff_alt_2) and len(self.seq_alt_2) > 2:
                 print("Signal of a diff {} for list  alternating 2. Next term is {}.".format(_correct_format(seq_diff_alt_2[0]), _correct_format(self.seq_alt_2[-1] + seq_diff_alt_2[0])))