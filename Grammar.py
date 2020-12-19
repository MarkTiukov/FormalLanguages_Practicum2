class Rule:
    rule_separator = "->"

    def __init__(self, rule_representation: str, rule_separator="->") -> None:
        super().__init__()
        Rule.rule_separator = rule_separator
        separator_position = rule_representation.find(rule_separator)
        self.begin = rule_representation[0]
        self.end = rule_representation[separator_position + len(rule_separator):]

    def __str__(self) -> str:
        return self.begin + Rule.rule_separator + self.end

    def __eq__(self, o: object) -> bool:
        return self.begin == o.begin and self.end == o.end


class Grammar:
    def __init__(self, rules=[], alphabet={'a', 'b', 'c'}) -> None:
        super().__init__()
        self.rules = rules
        self.alphabet = alphabet

    def __eq__(self, o: object) -> bool:
        return self.rules == o.rules

    def addRule(self, rule: Rule) -> None:
        self.rules.append(rule)

    def getRule(self, begin) -> list:
        appropriateRules = list()
        for rule in self.rules:
            if rule.begin == begin:
                appropriateRules.append(rule)
        return appropriateRules
