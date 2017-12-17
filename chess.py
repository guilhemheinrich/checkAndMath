import SolutionBranch
import Operator

teamA = (2,3,5,7,9,11,17,19,23)
teamB = (2,3,5,7,9,11,17,19,23)

# allOperator = {operatorAdd, operatorMinus, operatorMultiply, operatorDivide}

allOperator = {add, minus, multiply, divide}

root = SolutionBranch(alphabet = teamA)

root.generate(0, add)

def bloom(solutionBranch, operatorList):
