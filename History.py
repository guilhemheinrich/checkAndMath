



class History:
    def __init__(self, **kwargs):
        self.tabOperator = []
        self.tabValue = []
        if kwargs.has_key('history'):
            self.tabOperator = kwargs['history'].tabOperator[:]
            self.tabValue = kwargs['history'].tabValue[:]
    def addItem(self, operator, value):
        self.tabOperator.append(operator)
        self.tabValue.append(value)
    '''
    A key with the same operation in different order must be identical
    '''
    def getKey(self):
        return



