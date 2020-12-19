from Grammar import Rule, Grammar
from Parser import doesWordBelongToGrammar

if __name__ == "__main__":
    alphabet = {'(', ')'}
    rules = [Rule("U->S"), Rule("S->(S)S"), Rule("S->S(S)"), Rule("S->")]
    # rules = list()
    # inp = input()
    # while inp != "end":
    #     rules.append(Rule(inp))
    #     inp = input()
    grammar = Grammar(rules=rules)
    print(doesWordBelongToGrammar(word="((()())())", grammar=grammar))
