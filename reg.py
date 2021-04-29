import shuntingre
import thompson

if __name__ == "__main__":
    tests = [   ["(a.b|b*)",  ["ab", "b", "bb", "a"]]
    ]


with open('test.txt', 'r') as f:
    #words =  set(open('test.txt').read().split())
    list_of_lists = []
    for line in f:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    print(list_of_lists)
  

    for test in list_of_lists:
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