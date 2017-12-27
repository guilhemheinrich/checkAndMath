import SolutionBranch
import Operator
import History

# teamA = [2,3,5,7,9,11,17,19,23]
teamA = [2,3,5]
teamB = [2,3,5,7,9,11,17,19,23]

allOperator = (Operator.operatorAdd, Operator.operatorMinus, Operator.operatorMultiply, Operator.operatorDivide)

# allOperator = {operatorAdd, operatorAdd, operatorAdd, operatorAdd}

# hist = History.History()
# hist.tabOperator
root = SolutionBranch.SolutionBranch(alphabet = teamA)

# root.generate(0, Operator.operatorAdd)

allSolution = {}
root.bloom(allOperator, allSolution, 0)

def showDepth(depth):
    for sol in allSolution[depth]:
        print(sol.alphabet)

for sol in allSolution[1]:
    print(sol.history.tab_letters)