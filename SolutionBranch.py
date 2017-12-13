import History


class SolutionBranch:
    currentValue = 0
    currentAlphabet = list()
    currentHistory = History()


    # Copy constructor
    def __construct(self, solution):
        self.currentValue = solution.currentValue
        self.currentAlphabet = solution.currentAlphabet
        self.currentHistory = solution.currentHistory


    # Standard constructor
    def __construct(self, value, alphabet, hist):
        self.currentAlphabet = alphabet
        self.currentValue = value
        self.currentHistory = hist

    def generate(self, index, operation):
        assert index < self.currentAlphabet.__len__()
        nextValue = operation(self.currentValue, self.currentAlphabet[index])
        if (nextValue != None):
            nextAlphabet = self.currentAlphabet
            nextHistory = self.history
            nextHistory.tabValue.append(nextValue)
            nextHistory.tabOperator.append(operation.name)
            del nextAlphabet[-index]
            return SolutionBranch(nextValue, nextAlphabet)


