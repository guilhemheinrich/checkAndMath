import copy



class History:
    def __init__(self, **kwargs):
        self.tab_operators = []
        self.tab_letters = []
        if kwargs.has_key('history'):
            self.tab_operators = copy.copy(kwargs['history'].tab_operators)
            self.tab_letters = copy.copy(kwargs['history'].tab_letters)
    def addItem(self, operator, value):
        self.tab_operators.append(operator)
        self.tab_letters.append(value)
    '''
    A key with the same operation in different order must be identical
    '''
    def getKey(self):
        return



