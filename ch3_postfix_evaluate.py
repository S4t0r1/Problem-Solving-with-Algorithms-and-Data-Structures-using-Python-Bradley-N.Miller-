from pythonds.basic.stack import Stack


def evaluate_postfix(postfixStr):
    evalStack = Stack()
    opList = postfixStr.split()

    for token in opList:
        if token.isalnum():
            evalStack.push(int(token))
        else:
            operand2 = evalStack.pop()
            operand1 = evalStack.pop()
            result = calculate(token, operand1, operand2)
            evalStack.push(result)
    return evalStack.pop()


def calculate(operator, op1, op2):
    if operator in {"^", "**"}:
        return op1 ** op2
    elif operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2
    elif operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2


print(evaluate_postfix('7 8 + 3 2 + /'))
print(evaluate_postfix('17 10 + 3 * 9 /'))
print(evaluate_postfix("5 3 4 2 - ^ *"))
print(evaluate_postfix('5 3 44 22 - ** *'))
