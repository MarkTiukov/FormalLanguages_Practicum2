from Grammar import Rule, Grammar


class Situation:
    def __init__(self, rule: Rule, dot_position: int, begin_position: int) -> None:
        super().__init__()
        self.rule = rule
        self.begin_position = begin_position
        self.dot_position = dot_position

    def __eq__(self, o: object) -> bool:
        return self.rule == o.rule and self.begin_position == o.begin_position and self.dot_position == o.dot_position

    def isCompleted(self) -> bool:
        return self.dot_position == len(self.rule.end)

    def getCurrentSymbol(self) -> str:
        return self.rule.end[self.dot_position] if len(self.rule.end) > self.dot_position else ""


situations = list()


def doesWordBelongToGrammar(word: str, grammar: Grammar) -> bool:
    global situations
    generateSituations(grammar, word)
    first_rule = grammar.rules[0]
    final_situation = Situation(first_rule, 1, 0)
    return final_situation in situations[len(word)]


def generateSituations(grammar: Grammar, word: str) -> None:
    global situations
    situations = [list() for i in range(len(word) + 1)]
    first_rule = grammar.rules[0]
    situations[0].append(Situation(first_rule, 0, 0))
    current_size = -1
    while current_size != len(situations[0]):
        current_size = len(situations[0])
        predict(0, grammar)
        complete(0)
    for i in range(1, len(word) + 1):
        scan(i - 1, word[i - 1])
        current_size = -1
        while current_size != len(situations[i]):
            current_size = len(situations[i])
            predict(i, grammar)
            complete(i)


def predict(situation_number: int, grammar: Grammar) -> None:
    global situations
    new_situations = list()
    for situation in situations[situation_number]:
        start_symbol = situation.getCurrentSymbol()
        for rule in grammar.getRule(start_symbol):
            new_situations.append(Situation(rule, 0, situation_number))
    for situation in new_situations:
        if situation not in situations[situation_number]:
            situations[situation_number].append(situation)


def complete(situation_number: int) -> None:
    global situations
    new_situations = list()
    for situation in situations[situation_number]:
        if situation.isCompleted():
            for possible_situation in situations[situation.begin_position]:
                if possible_situation.getCurrentSymbol() == situation.rule.begin:
                    new_situations.append(Situation(possible_situation.rule,
                                                    possible_situation.dot_position + 1,
                                                    possible_situation.begin_position))
    for situation in new_situations:
        if situation not in situations[situation_number]:
            situations[situation_number].append(situation)


def scan(situation_number: int, symbol: str) -> None:
    global situations
    for situation in situations[situation_number]:
        if symbol == situation.getCurrentSymbol():
            situations[situation_number + 1].append(
                Situation(situation.rule, situation.dot_position + 1, situation.begin_position))


def fit(line1: str, line2: str, line3: str, line4: str) -> (str, Grammar):
    alphabet = set(line1)
    separator = line2
    if separator == "":
        separator = Rule.rule_separator
    rules = [Rule(rule, separator) for rule in line3.split()]
    grammar = Grammar(rules, alphabet)
    return line4, grammar


if __name__ == "__main__":
    print("YES" if doesWordBelongToGrammar(*fit(input(), input(), input(), input())) else "NO")
