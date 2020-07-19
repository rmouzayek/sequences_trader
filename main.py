from utils import _hide_numpy_warnings
from reader import Reader
from functions import Functions
from table import Table
from detector import Detector 



class Main:
    def __init__(self, *reader_input):
        self.input= reader_input
        self.sequence = Reader(reader_input).get_sequence()
        self.functions = Functions()
        
    def _display_tables(self):
        main_table = Table(self.sequence, self.functions, 'Main table')
        table_alternate_1 = Table(self.sequence[0::2], self.functions, 'Table for the Sequence alternate 1')
        table_alternate_2 = Table(self.sequence[1::2], self.functions,  ' Table for the Sequence alternate 2')
        main_table.display()
        table_alternate_1.display()
        table_alternate_2.display()
    
    def _search_for_signals(self):
        Detector(self.sequence)()
        
    def __call__(self):
        _hide_numpy_warnings()
        
        self._search_for_signals()
        self._display_tables()
        
        
        
        
if __name__ == '__main__':    
    Test = [[54, 54, 3, 6 ,8], [2, 3, 4, 9 , 6, 27], " 55  --   91  --  19  --  31  --  7  --  11  --", "3  --  9  --  13  --  11  --  33  --  37", "5  --  4  --  9  --  0  --  13  --  -4", "3  --  4  --  7  --  16  --  11  --  64 ", "3  --  4  --  7  --  11  --  18  --  29  ", "3  --  4  --  7  --  11  --  18  --  29  ", "3 13  --  4 12  --  6 10  --  9 7  --  ", " 49  --  8   --  41  --  10  --  31  --  15", "114  --  38  --  19  --  18  --  6  --  3  ", "5  --  7  --  14  --  16  --  32  --  34 ", "8  --  14  --  13  --  7  --  9  --  15  --  12   ", "-2 5 -4 3 -6"]
    for test in Test:
        Main(test)()


