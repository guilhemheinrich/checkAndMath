import copy
import Operator


class History:
    def __init__(self, **kwargs):
        self.tab_operators = []
        self.tab_letters = [0]
        self.symetric_operators = []
        if kwargs.has_key('history'):
            self.tab_operators = copy.copy(kwargs['history'].tab_operators)
            self.tab_letters = copy.copy(kwargs['history'].tab_letters)
            self.symetric_operators = kwargs['history'].symetric_operators
    def addItem(self, operator, value):
        self.tab_operators.append(operator)
        self.tab_letters.append(value)
    # def toString(self):
        
    '''
    A key with the same symetric operation in different order must be identical
    '''
    def getKey(self):
        # Ordering 
        string_tab = []
        last_operator = self.tab_operators[0]
        orderedLetters = [self.tab_letters[0]]
        for index in range(self.tab_operators.__len__()):
            operator = self.tab_operators[index]
            if last_operator == operator:
                orderedLetters.append(self.tab_letters[index + 1])
            else:
                ol_size = orderedLetters.__len__()
                if ol_size > 1:
                    orderedLetters.sort()
                string_tab.append(str(orderedLetters[0]))
                for subindex in range(ol_size - 1):
                    string_tab.append(last_operator.name)
                    string_tab.append(str(orderedLetters[subindex + 1]))
                string_tab.append(operator.name)
                orderedLetters = [self.tab_letters[index + 1]]
            last_operator = operator
        ol_size = orderedLetters.__len__()
        if ol_size > 1:
            orderedLetters.sort()
        string_tab.append(str(orderedLetters[0]))
        for subindex in range(ol_size - 1):
            string_tab.append(last_operator.name)
            string_tab.append(str(orderedLetters[subindex + 1]))
        return '_'.join(string_tab)



