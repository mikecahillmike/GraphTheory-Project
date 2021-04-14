# Adapted from the pseudocode @:
# https://en.wikipedia;.org/wiki/Shunting-yard_algorithm

def shunt(infix):
    """Cobert infix expressions o postfix"""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack
    stack = ""
    # Operator precedence (Dictionary)
    prec = {'*': 100, '/': 90, '+': 80, '-': 70, '(': 60, ')': 50}
    for c in infix: # loop through string one char at a time 
        if c in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            # Push to output
            postfix = postfix + c
        # if c is an opperator
        elif c in {'+', '-', '*', '/'}:
            # Check what is on the stack
            while len(stack) > 0 and prec[stack[-1]] > prec[c] and stack[-1] != '(':
                #pop
                # Append operator at the top of stack to output
                postfix = postfix + stack[-1]
                # Remove operator from stack
                stack = stack[:-1]
            # Push c to stack
            stack = stack + c
        elif c == '(':
            # Push c to stack
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                #pop
                # Append operator at the top of stack to output
                postfix = postfix + stack[-1]
                # Remove operator from stack
                stack = stack[:-1]
            # Remove open bracket from from stack
            stack = stack[:-1]
    while len(stack)!=0:
        #pop
        # Append operator at the top of stack to output
        postfix = postfix + stack[-1]
        # Remove operator from stack
        stack = stack[:-1]
    return postfix


infix = "3+4*(2-1)"
postfix = "3421-*+"

print(f"infix: {infix}")
print(f"shunt: {shunt(infix)}")
print(f"postfix: {postfix}")