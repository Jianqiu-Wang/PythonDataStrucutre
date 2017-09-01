from stack import Stack

# Evaluate postfix expression
# Input: a postfix string with space between any 2 consecutive operands
def postfix_eval(postfix_str):
    operand_stack = Stack()
    postfix_list = postfix_str.split()
    for token in postfix_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        elif token in "+-*/":
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            # Calculate and push result into stack
            operand_stack.push(do_math(token, operand1, operand2))

    return operand_stack.pop()


def do_math(token, operand1, operand2):
    if token == "+":
        return operand1 + operand2
    elif token == "-":
        return operand1 - operand2
    elif token == "*":
        return operand1 * operand2
    elif token == "/":
        return operand1 / openrand2

# Test cases
print(postfix_eval("2 3 - 6 * "))
print(postfix_eval("2 3 * 6 - 9 + "))
