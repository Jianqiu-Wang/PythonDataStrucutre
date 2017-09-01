# Infix to postfix
from stack import Stack

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["^"] = 1
    prec["("] = 0

    op_stack = Stack() # operator stack, only +-*/ and () can be pushed
    postfix_list = []
    infix_list = infix_expr.split()
    operand = "ABCEDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for token in infix_list:
        print(token)
        if token in operand: # characters and numbers
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token) # push (
        elif token == ')':
            temp_top = op_stack.pop() # pop until ( appears
            while temp_top != '(':
                postfix_list.append(temp_top)
                temp_top = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                  (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token) # push +-*/

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

# Test cases
print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("5 * 3 ^ ( 4 − 2 )"))
