import shuntingre
import thompson

if __name__ == "__main__":
    tests = [   ["(a.b|b*)",    ["ab", "b", "bb", "a"]]
            ,   ["a.(b.b)*.a",  ["aa", "abba", "aba"]]
           # ,   ["1.(0.0)*.1",  ["11", "100001", "11001"]] 
    ]

# with open('file.txt, 'r') as f:
    # Read a line of f.
    # See if it matches the regular expression
    # if it does print the line

    for test in tests:
        infix = test[0]
        print(f"infix:  {infix}")
        postfix = shuntingre.shunt(infix)
        print(f"postfix: {postfix}")
        nfa = thompson.re_to_nfa(postfix)
        print(f"thompson: {nfa}")
        for s in test[1]:
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
        print()