import SolutionBranch
import Operator
import History

# teamA = [2,3,5,7,9,11,17,19,23]
teamA = [2,3,5,7,9,11]
teamB = [2,3,5,7,9,11,17,19,23]

allOperator = (Operator.operatorAdd, Operator.operatorMinus, Operator.operatorMultiply, Operator.operatorDivide)
symetricOperator = (Operator.operatorAdd, Operator.operatorMinus, Operator.operatorMultiply)

root = SolutionBranch.SolutionBranch(alphabet = teamA, targets_value = teamB)

# root.generate(0, Operator.operatorAdd)

allSolution = {}
for key in teamB:
    allSolution[key] = {}

root.bloom(allOperator, allSolution, 0)

allSolution[11][2][0].history.getKey()

for index, key in enumerate(allSolution[11][2]):
    print((index, key))


def showDepth(depth):
    for sol in allSolution[depth]:
        print(sol.alphabet)

for sol in allSolution[1]:
    print(sol.history.tab_letters)