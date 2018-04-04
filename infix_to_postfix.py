from pythonds.basic.stack import Stack

def convertToPostfix(infixStr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    infixList = infixStr.split()
    correctData(infixList)

    for token in infixList:
        if len(token) > 1:
            postfixList.append(token)
            continue
        if token in "0123456789ABCDEFGHIJKLMNOPRSTUVWXYZ":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and  \
            prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)
    while (not opStack.isEmpty()):
        postfixList.append(opStack.pop())
    postfixstr = " ".join(postfixList)
    return postfixstr


def correctData(infixList):
    """This is a bonus function. It cleans the data in such a way
        so that it does not matter if you have spaces between the
        operands and parentheses, or multi-digit numbers or both."""

    for index, token in enumerate(infixList):
        if len(token) > 1 and (not token.isalnum()):
            if len(token) >= 3:
                rear_index = index + token.index(token[-1])
                newindex, i = (rear_index, -1) if token[:-1].isalnum() else (index, +1)
                parenth, rest = (token[0], token[1:]) if token[1:].isalnum() \
                           else (token[-1], token[:-1])
                infixList.insert(newindex, parenth)
                infixList.insert(newindex + i, rest)
            else:
                for subindex, subtoken in enumerate(token):
                    infixList.insert(index + subindex, subtoken)
            infixList.remove(token)
    return infixList


print(convertToPostfix("A * B + C * D"))
print(convertToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(convertToPostfix("5 * 3 ^ ( 4 - 2 )"))
print(convertToPostfix("A * BC + CD * D"))
print(convertToPostfix("(A + B) * C - (D - E) * (FO + GI)"))
print(convertToPostfix("5 * 32 ^ (444 - 22)"))
