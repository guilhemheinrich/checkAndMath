import History
import copy


class SolutionBranch:
    
    def __init__(self, **kwargs):
        self.value = 0
        self.alphabet = None
        self.history = History.History()
        self.target_value = None
        if kwargs.has_key('target_value'):
            self.target_value = kwargs['target_value']
        if kwargs.has_key('alphabet'):
            self.alphabet = copy.copy(kwargs['alphabet'])
        if kwargs.has_key('value'):
            self.value = kwargs['value']
        if kwargs.has_key('history'):
            self.history = copy.copy(kwargs['history'])
        if kwargs.has_key('solution'):
            self.alphabet = kwargs['solution'].alphabet[:]
            self.value = kwargs['solution'].value
            self.history = kwargs['solution'].history
            self.target_value = kwargs['solution'].target_value
        
    def generate(self, index, operator):
        assert index < self.alphabet.__len__()
        nextValue = operator.compute(self.value, self.alphabet[index])
        if (nextValue != None) and (nextValue > 0):
            nextAlphabet = copy.copy(self.alphabet)
            nextHistory = History.History(history = self.history)
            nextHistory.tab_letters.append(self.alphabet[index])
            nextHistory.tab_operators.append(operator)
            del nextAlphabet[index]
            nextBranch = SolutionBranch(value = nextValue, alphabet = nextAlphabet, history = nextHistory, target_value = self.target_value)
            # print('___________________________________')
            # print('current alphabet')
            # print(self.alphabet)
            # print(' I picked [index] = ' + str(index) + 'which is ' + str(self.alphabet[index]) )
            # print('nextAlphabet')
            # print(nextBranch.alphabet)
            # print("current history.tab_letters")
            # print(nextBranch.history.tab_letters)
            return nextBranch

    def bloom(self, operatorList, solutionList, depth):
        for ope in operatorList:
            for index in range(self.alphabet.__len__()):
                # print(index)
                newBranch = self.generate(index, ope)
                if newBranch != None:
                    if not (depth in solutionList):
                        solutionList[depth] = []
                    solutionList[depth].append(newBranch)
                    newBranch.bloom(operatorList, solutionList, depth + 1)
                    # print(newBranch.value)




