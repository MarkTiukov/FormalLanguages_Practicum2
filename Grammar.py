rule_separator = "->"


class Rule:
    def __init__(self, rule_representation: str) -> None:
        super().__init__()
        separator_position = rule_representation.find(rule_separator)
        self.begin = rule_representation[0]
        self.end = rule_representation[separator_position + len(rule_separator):]

    def __str__(self) -> str:
        return self.begin + rule_separator + self.end

    def __eq__(self, o: object) -> bool:
        return self.begin == o.begin and self.end == o.end


class Grammar:
    def __init__(self, rules=[], alphabet={'a', 'b', 'c'}) -> None:
        super().__init__()
        self.rules = rules
        self.alphabet = alphabet

    def addRule(self, rule: Rule) -> None:
        self.rules.append(rule)

    def getRule(self, begin) -> list:
        appropriateRules = list()
        for rule in self.rules:
            appropriateRules.append(rule)
        return appropriateRules
