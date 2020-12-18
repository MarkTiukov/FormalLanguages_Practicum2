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


class Parser:
    def __init__(self, grammar: Grammar, word: str) -> None:
        super().__init__()
        self.situations = [set()] * (len(word) + 1)
        starting_rule = grammar.rules[0]
        self.situations[0].add(Situation(starting_rule, 0, 0))
        current_size = -1
        while current_size != len(self.situations[0]):
            current_size = len(self.situations[0])
            self.predict(0, grammar)
            # complete(0)

    def predict(self, situation_number: int, grammar: Grammar):
        for situation in self.situations[situation_number]:
            start_symbol = situation.getCurrentSymbol()
            for rule in grammar.getRule(start_symbol):
                self.situations[situation_number].add(Situation(rule, 0, situation_number))
