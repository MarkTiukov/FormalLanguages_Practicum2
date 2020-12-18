from Grammar import Rule, Grammar


class Situation:
    def __init__(self, rule: Rule, begin_position: int, dot_position: int) -> None:
        super().__init__()
        self.rule = rule
        self.begin_position = begin_position
        self.dot_position = dot_position

    def isCompleted(self) -> bool:
        return self.dot_position == len(self.rule.end)

    def getCurrentSymbol(self) -> str:
        return self.rule.end[self.dot_position]


situations = list()


def generateSituations(grammar: Grammar, word: str) -> None:
    global situations
    situations = [set()] * (len(word) + 1)
    starting_rule = grammar.rules[0]
    situations[0].add(Situation(starting_rule, 0, 0))
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


def predict(situation_number: int, grammar: Grammar):
    global situations
    for situation in situations[situation_number]:
        start_symbol = situation.getCurrentSymbol()
        for rule in grammar.getRule(start_symbol):
            situations[situation_number].add(Situation(rule, 0, situation_number))


def complete(situation_number: int):
    global situations
    for situation in situations[situation_number]:
        if situation.isCompleted():
            for possible_situation in situations[situation.begin_position]:
                if possible_situation.getCurrentSymbol() == situation.rule.begin:
                    situations[situation_number].add(Situation(possible_situation.rule,
                                                               possible_situation.dot_position + 1,
                                                               possible_situation.begin_position))


def scan(situation_number: int, symbol: str):
    global situations
    for situation in situations[situation_number]:
        if situation == situation.getCurrentSymbol():
            situations[situation_number + 1].add(Situation(situation.rule, situation.dot_position + 1, situation.begin_position))
