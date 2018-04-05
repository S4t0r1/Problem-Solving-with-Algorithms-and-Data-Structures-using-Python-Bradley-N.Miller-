# Tells if symbols inside a string are balanced, there are two similiar but slightly different algorithms
# 1st approach

from pythonds.basic.stack import Stack


def balanced(inputStr):
    opeStack = Stack()
    balanced = True
    for char in inputStr:
        if char in "({[<":
            opeStack.push(char)
        else:
            if opeStack.isEmpty() or (not matches(opeStack.peek(), char)):
                balanced = False
                return balanced
            opeStack.pop()

    if not opeStack.isEmpty():
        balanced = False
    return balanced


def matches(open, close):
    openers = "({[<"
    closers = ")}]>"
    return openers.index(open) == closers.index(close)


print(balanced("((()))"))
print(balanced("((())))"))
print(balanced("[(<({})()>)]"))
print(balanced("[<(({})()>)]"))

#=========================================================================================================================
# 2nd approach...

from pythonds.basic.stack import Stack


def balanced(symbolStr):
    opeStack = Stack()
    balanced = True
    index = 0
    while index < len(symbolStr) and balanced:
        char = symbolStr[index]
        if char in "({[<":
            opeStack.push(char)
        else:
            if opeStack.isEmpty():
                balanced = False
            else:
                top = opeStack.pop()
                if not matches(top, char):
                    balanced = False
        index += 1

    if opeStack.isEmpty() and balanced:
        return True
    else:
        return False


def matches(open, close):
    openers = "({[<"
    closers = ")}]>"
    return openers.index(open) == closers.index(close)


print(balanced("((()))"))
print(balanced("((())))"))
print(balanced("[(<({})()>)]"))
print(balanced("[<(({})()>)]"))
