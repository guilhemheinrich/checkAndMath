import copy
import Operator


class History:
    symetric_operators = []
    inverse_operators = {}
    def __init__(self, **kwargs):
        self.tab_operators = []
        self.tab_letters = [0]
        self.ordered_operators = []
        self.ordered_letters = []
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
        string_tab = [str(self.tab_letters[0])]
        if len(self.tab_operators) == 0:
            return 'NA'
        last_operator = self.tab_operators[0]
        orderedLetters = []
        orderedOperatorsName = []
        for index in range(self.tab_operators.__len__()):
            operator = self.tab_operators[index]
            # Check if the opertor is symetric
            if (last_operator == operator) and (operator in History.symetric_operators):
                orderedLetters.append(self.tab_letters[index + 1])
                orderedOperatorsName.append(operator.name)
            elif last_operator in History.inverse_operators.keys() and History.inverse_operators[last_operator] == operator:
                orderedLetters.append(self.tab_letters[index + 1])
                orderedOperatorsName.append(operator.name)
            else:
                if len(orderedLetters) == 0:
                    self.ordered_operators.append(operator.name)
                    self.ordered_letters.append(self.tab_letters[index + 1])
                else:
                    sortedLetters, sortedOperators = self.__reorder(orderedLetters, orderedOperatorsName)
                    self.ordered_operators += sortedOperators
                    self.ordered_letters += sortedLetters
                    orderedOperatorsName = [operator.name]
                    orderedLetters = [self.tab_letters[index + 1]]
                # ol_size = sortedLetters.__len__()
                # if ol_size > 1:
                #     orderedLetters.sort()
                # string_tab.append(str(sortedLetters[0]))
                # for subindex in range(ol_size):
                #     string_tab.append(sortedOperators[subindex])
                #     string_tab.append(str(sortedLetters[subindex]))
                    # print(sortedOperators[subindex])
                    # print(str(sortedLetters[subindex]))
                # string_tab.append(operator.name)
            last_operator = operator
        # if ol_size > 1:
        #     orderedLetters.sort()    
        if len(orderedLetters) == 0:
            self.ordered_operators.append(operator.name)
            self.ordered_letters.append(self.tab_letters[index + 1])
        else:
            sortedLetters, sortedOperators = self.__reorder(orderedLetters, orderedOperatorsName)
            self.ordered_operators += sortedOperators
            self.ordered_letters += sortedLetters
        ol_size = self.ordered_letters.__len__()
        # string_tab.append(str(sortedLetters[0]))
        # Cas particulier du 0 + x * y = 0 + y * x etc
        # print(len(sortedOperators))
        if len(self.ordered_operators) > 1:
            # print(self.ordered_operators)
            # print(sortedLetters)
            # print(self.ordered_operators[0])
            # print(self.ordered_operators[1])
            # print(self.ordered_operators[1] in [x.name for x in History.symetric_operators])
            if self.ordered_operators[0] != self.ordered_operators[1] and self.ordered_operators[1] in [x.name for x in History.symetric_operators]:
                if self.ordered_letters[0] > self.ordered_letters[1]:
                    mem = self.ordered_letters[0]
                    self.ordered_letters[0] = self.ordered_letters[1]
                    self.ordered_letters[1] = mem
                    # print(sortedLetters)
        # print(self.ordered_operators)       
        # print(self.ordered_letters)       
        for subindex in range(ol_size):
            # print(sortedOperators[subindex])
            # print(str(sortedLetters[subindex]))            
            string_tab.append(self.ordered_operators[subindex])
            string_tab.append(str(self.ordered_letters[subindex]))
        return '_'.join(string_tab)
    '''
    Function to reorder the letters (values) / operation 
    If there is an inverse function, both components should be sorted and the merged
    '''
    def __reorder(self, orderedLetters, orderedOperatorsName):
        # print(orderedLetters)
        # print(orderedOperatorsName)
        sortedLetters = copy.copy(orderedLetters)
        sortedOperatorsName = copy.copy(orderedOperatorsName)
        sortOperators = sorted( range(len(orderedOperatorsName)), key = lambda k : orderedOperatorsName[k])
        for i in sortOperators:
            sortedLetters[i] = orderedLetters[sortOperators[i]]
            sortedOperatorsName[i] = orderedOperatorsName[sortOperators[i]]
        lastOpe = sortedOperatorsName[0]
        for k in range(len(sortedOperatorsName)):
            if sortedOperatorsName[k] != lastOpe:
                break
            lastOpe = sortedOperatorsName[k]
        olA = sortedLetters[:k]
        olB = sortedLetters[k:]
        olA.sort()
        olB.sort()
        return olA+olB, sortedOperatorsName
    def buildSet(self):
        self.set_letters = set()
        for letter in self.ordered_letters:
            self.set_letters.add(letter)


        







# orderedOperatorsName = ['+', '+', '-', '+', '+', '-']
# orderedLetters = [2, 5, 7, 11, 3, 13, 9]

# sorted( range(len(orderedOperatorsName)), key = lambda k : orderedOperatorsName[k])