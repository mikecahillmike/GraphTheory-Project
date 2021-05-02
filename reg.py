import shuntingre
import thompson

with open('test.txt', 'r') as f:
    #words =  set(open('test.txt').read().split())
    # Adapted from
    # https://www.kite.com/python/answers/how-to-convert-each-line-in-a-text-file-into-a-list-in-python?fbclid=IwAR0woOBg8shV2w2kBgT_Yitn2wrA9GRwMfTJD18DY1DCpnbW0Eu1wdYYlCU
    list_of_lists = []
    for line in f:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    print(list_of_lists)
    ##########

for test in list_of_lists:
    infix = test[0]
    i = 1
    print(f"infix:  {infix}")
    postfix = shuntingre.shunt(infix)
    print(f"postfix: {postfix}")
    nfa = thompson.re_to_nfa(postfix)
    print(f"thompson: {nfa}")
    # loop through list
    while test:
        s = test[i]
        match = nfa.match(s)
        print(f"Match '{s}': {match}")
        # if list matches end then end of list
        if test[i] == test[-1]:
            # Adapted from
            # https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3
            break
        i+=1
    print()