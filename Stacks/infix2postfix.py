from Stacks.Stack import Stack


def infix2postfix(infixexpr):
    """
    Transform a infix compression to its equivalent postfix compression
    infixexpr: A infix math compression consists of elementary arithmetic
    wherein each operator and operand should be split by SPACE.
    """
    prec = {"*": 3, '/': 3, '+': 2, '-': 2, '(': 1}
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


if __name__ == "__main__":
    print(infix2postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
