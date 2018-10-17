from Stacks.infix2postfix import *


def op(op, op1, op2):
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1 - op2
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2


def eval_postfix(postfix: str):
    tokens = postfix.split(' ')

    valstack = Stack()
    for token in tokens:
        if token in '0123456789':
            valstack.push(int(token))
        if token in '+-*/':
            # the operand pushed earlier appears earlier in the expression
            # example AB- push A(operand1), then push B(operand2)
            operand2 = valstack.pop()
            operand1 = valstack.pop()
            temp = op(token, operand1, operand2)
            valstack.push(temp)
    return valstack.pop()


if __name__ == '__main__':
    infix = '( 5 + 5 ) * 5 - 8 / ( 3 + 1 )'  # 48
    postfix = infix2postfix(infix)
    print(infix, '\n', postfix)
    print(eval_postfix(postfix))
