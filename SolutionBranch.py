import History


class SolutionBranch:
    attributes = {'value', 'alphabet', 'history'}
    
    def __init__(self, **kwargs):
        self.value = 0
        self.hist = None
        self.history = None
        if kwargs.has_key('alphabet'):
            self.alphabet = kwargs['alphabet']
        if kwargs.has_key('value'):
            self.value = kwargs['value']
        if kwargs.has_key('history'):
            self.history = kwargs['history']
        if kwargs.has_key('solution'):
            self.alphabet = kwargs['solution'].alphabet
            self.value = kwargs['solution'].value
            self.hist = kwargs['solution'].hist
        
    def generate(self, index, operation):
        assert index < self.alphabet.__len__()
        nextValue = operation(self.value, self.alphabet[index])
        if nextValue != None:
            nextAlphabet = self.alphabet
            nextHistory = self.history
            nextHistory.tabValue.append(nextValue)
            nextHistory.tabOperator.append(operation.name)
            del nextAlphabet[-index]
            return SolutionBranch(value = nextValue, alphabet = nextAlphabet)


