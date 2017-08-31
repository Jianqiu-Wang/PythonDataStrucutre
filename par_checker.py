from stack import Stack

# Completed extended par_checker for: [,{,(,),},]
def par_checker(symbol_string):
    """  Loop over symbol_string, if symbol is (, push to stack,
    if symbol is ) , check whether there is a ( to match with,
        if so, pop from stack,
        o.w., unbalanced parathensis
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(closes) # list, O(1)

print(par_checker('((()))'))
print(par_checker('(()'))
print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))
