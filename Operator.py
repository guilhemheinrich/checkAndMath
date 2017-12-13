
class Operator:
    binaryOperator = '+'
    name = 'plus'

    def __new__(cls, *args, **kwargs):
        

    def __init__(self, member):
        self.binaryOperator = binaryOperator
        self.name = name


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if x % y == 0:
        return x / y
    else:
        return None


operatorAdd = Operator(add, '+')
operatorMinus = Operator(minus, '-')
operatorMultiply = Operator(multiply, '*')
operatorDivide = Operator(divide, '/')
