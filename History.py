import copy
import Operator


class History:
    symetric_operators = []
    inverse_operators = {}
    def __init__(self, **kwargs):
        self.tab_operators = []
        self.tab_letters = [0]
        if kwargs.has_key('history'):
            self.tab_operators = copy.copy(kwargs['history'].tab_operators)
            self.tab_letters = copy.copy(kwargs['history'].tab_letters)
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
        orderedOperatorsName = []
        for index in range(self.tab_operators.__len__()):
            operator = self.tab_operators[index]
            # Check if the opertor is symetric
            if (last_operator == operator) and (operator in History.symetric_operators):
                orderedLetters.append(self.tab_letters[index + 1])
                orderedOperatorsName.append(operator.name)
            elif last_operator in History.symetric_operators and History.symetric_operators[last_operator] == operator:
                orderedLetters.append(self.tab_letters[index + 1])
                orderedOperatorsName.append(operator.name)
            else:
                self.reorder(orderedLetters, orderedOperatorsName)
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
        self.reorder(orderedLetters, orderedOperatorsName)
        return '_'.join(string_tab)
    '''
    Function to reorder the letters (values) / operation 
    If there is an inverse function, both components should be sorted and the merged
    '''
    def reorder(self, orderedLetters, orderedOperatorsName):
        pass



# orderedOperatorsName = ['+', '+', '-', '+', '+', '-']
# orderedLetters = [2, 5, 7, 11, 3, 13, 9]

# sorted( range(len(orderedOperatorsName)), key = lambda k : orderedOperatorsName[k])