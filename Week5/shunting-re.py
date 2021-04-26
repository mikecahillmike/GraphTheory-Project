# Adapted from the pseudocode @:
# https://en.wikipedia;.org/wiki/Shunting-yard_algorithm

def shunt(infix):
    """Cobert infix expressions o postfix"""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack
    stack = ""
    # Operator precedence (Dictionary)
    prec = {'*': 100, '.': 90, '|': 80, '(': 70, ')': 60}
    # loop through string one char at a time 
    for c in infix: 
        
        if c in {'a', 'b'}:
            # Push to output
            postfix = postfix + c
        # if c is a non-special
        elif c in {'*', '.', '|'}:
            # Check what is on the stack
            while len(stack) > 0 and prec[stack[-1]] != '(' and prec[stack[-1]] >= prec[c]:
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

if __name__ == "__main__":
    for infix in ["a.(b.b)*.a"]:
        print(f"infix: {infix}")
        print(f"shunt: {shunt(infix)}")
        print()