import SolutionBranch
import Operator
import History

# teamA = [2,3,5,7,9,11,17,19,23]
teamA = [2,3,5,7]
teamB = [2,3,5,7,9,11,17,19,23]

allOperator = (Operator.operatorAdd, Operator.operatorMinus, Operator.operatorMultiply, Operator.operatorDivide)
symetricOperator = (Operator.operatorAdd, Operator.operatorMultiply)
inverseOperator ={ Operator.operatorAdd : Operator.operatorMinus, Operator.operatorMinus : Operator.operatorAdd }
History.History.symetric_operators = symetricOperator
History.History.inverse_operators = inverseOperator

root = SolutionBranch.SolutionBranch(alphabet = teamA, targets_value = teamB)
# root.history.symetric_operators = symetricOperator
# root.generate(0, Operator.operatorAdd)

allSolution = {}
for key in teamB:
    allSolution[key] = {}

root.history.getKey()
root.bloom(allOperator, allSolution, 0)
allSolution[11][2]['0_+_3_*_2_+_5'].history.getKey()

for index, key in enumerate(allSolution[11][2]):
    print((index, key))
    print(allSolution[11][2][key].history.symetric_operators)

for sol in allSolution[11][2]:
    print(sol.history.symetric_operators)


def showDepth(depth):
    for sol in allSolution[depth]:
        print(sol.alphabet)

for sol in allSolution[1]:
    print(sol.history.tab_letters)