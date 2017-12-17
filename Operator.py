
class Operator:
    def __init__(self, **kwargs):
        if kwargs.has_key('binaryOperator'):
            self.binaryOperator = kwargs['binaryOperator']
        if kwargs.has_key('name'):
            self.name = kwargs['name']


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


operatorAdd = Operator(binaryOperator = add, name = '+')
operatorMinus = Operator(binaryOperator = minus, name = '-')
operatorMultiply = Operator(binaryOperator = multiply, name = '*')
operatorDivide = Operator(binaryOperator = divide, name = '/')
