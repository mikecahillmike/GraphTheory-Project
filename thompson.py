# Thompson's Construction.

class State:
    """A state and its arrows in Thompson's construction."""
    # Constructor
    def __init__(self, label, arrows, accept):
        """Label is the arrow labels, arrows is a list of states to
           point to, accept is a boolean as to whether this is an accept
           state.
        """
        self.label = label
        self.arrows = arrows
        self.accept = accept

    def followes(self):
        """The set of states that are gotten from following this state
            and all its e arrows"""
        # Include this state in the returned set
        states = {self}
        # If this state has e arrows, i.e is None
        if self.label is None:
            # Loop through this state's arrows
            for state in self.arrows:
                # Incorporate that states e arrow states in states.
                states = (states | state.followes())
        # Return the set of states.
        return states

class NFA:
    """A non-deterministic finate automation"""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def match(self, s):
        """Retrun True if this NDA (instance) matches the string s."""
        # A list of previous states that we are still in
        previous = self.start.followes()
        # Loop through the string. a charachter at a time
        for c in s:
            # Start with an empty set of current states
            current = set()
            # Loop through the previous state
            for state in previous:
                # Check if there is a c arrow from state
                if state.label == c:
                    # Add followes for nect state.
                    current = (current | state.arrows[0].followes())
            # Replace previous with current
            previous = current
        # If the final state is in previous, then return True, False otherwise
        return (self.end in previous)


def re_to_nfa(postfix):
    # A stack for NFAs.
    stack = []
    # Loop through the postfix r.e. left to right
    for c in postfix:
        # Concatenation.
        if c == ".":
            # Pop top NFA off the stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the rest next NFA off stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Make accept state of NFA1 non accept.
            nfa1.end.accept = False
            # Make it point at start state of nfa2
            nfa2.end.arrows.append(nfa2.start)
            # Make a new NFA with nfa1's start state and nfa2's end state.
            nfa = NFA(nfa1.start, nfa2.end)
            # Push to the stack
            stack.append(nfa)
        elif c == "|":
            # Pop top NFA off the stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end state
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start states.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make old end states non accept.
            nfa1.end.accept = False
            nfa2.end.accept = False
            # Point old end states to new one.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # Make a new NFA 
            nfa = NFA(start, end)
            # Push to the stack
            stack.append(nfa)
        elif c == '*':
            # Pop one NFA off stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end state
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start state.
            start.arrows.append(nfa1.start)
            # and at the new end state
            start.arrows.append(end)
            # Make old end state non accept.
            nfa1.end.accept = False
            # Make old end state point to new end state.
            nfa1.end.arrows.append(end)
            # Make old end state point to new start state.
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA 
            nfa = NFA(start, end)
            # Push to the stack
            stack.append(nfa)
        else:
            # Create an NFA for the non-special character c
            # Create the end state
            end = State(None, [], True)
            # Create the start state, pointed at the end state
            start = State(c, [], False)
            # Point new start state at the new end state
            start.arrows.append(end)
            # Create the NFA with the start and end state
            nfa = NFA(start, end)
            # Append the NFA to the NFA stack
            stack.append(nfa)

    # There should only be one NFA on the stack
    if len(stack) != 1:
        return None
    else:
        return stack[0]

if __name__ == "__main__":
    for postfix in ["abb,*.a.", "100.*.1.", 'ab|']:
        print(f"postfix: {postfix}")
        print(f"nfa:     {re_to_nfa(postfix)}")
        print()