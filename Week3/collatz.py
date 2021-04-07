"""Verifiying the Collatz conjecture"""
# Michael Cahill

def f(n):
    # if n is even
    if n % 2 == 0:
        return n // 2 # no decimal (divide int)
    # if n is odd
    elif n % 2 == 1:
        return (3 * n) + 1
    else:
        return None


def collatz(n):
    # Prevent infinate loop
    so_far = []
    # Loop until n is 1
    while n != 1:
        if n in so_far: # check for same value
            return False
        so_far.append(n)
        n = f(n)
    so_far.append(n)
    return so_far

#print(collatz(10))
print(collatz(27))