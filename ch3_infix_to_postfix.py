from pythonds.basic.stack import Stack

def convertToPostfix(infixStr):
    """This function converts a given infix string into
       a postfix string..

       >>> print(convertToPostfix("A * B + C * D"))
       A B * C D * +
       >>> print(convertToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
       A B + C * D E - F G + * -
       >>> print(convertToPostfix("5 * 3 ^ ( 4 - 2 )"))
       5 3 4 2 - ^ *
    """

    prec = {}
    prec["^"], prec["**"] = 4, 4
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
        if len(token) > 1 and token.isalnum():
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
    """ This is a bonus function. It cleans the data in such a way
        so that it does not matter if you have spaces between the
        operands and parentheses, or multi-digit numbers or both.

        >>> print(convertToPostfix("A * BC + CD * D"))
        A BC * CD D * +
        >>> print(convertToPostfix("(A + B) * C - (D - E) * (FO + GI)"))
        A B + C * D E - FO GI + * -
        >>> print(convertToPostfix("5 * 32 ^ (444 - 22)"))
        5 32 444 22 - ^ *
    """

    for index, token in enumerate(infixList):
        if len(token) > 1 and (not token.isalnum()) and token != "**":
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
print(convertToPostfix("5 * 32 ** (444 - 22)"))
