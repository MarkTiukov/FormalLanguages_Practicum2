rule_separator = "->"


class Rule:

    def __init__(self, rule=None) -> None:
        super().__init__()
        if (rule == None):
            self.begin = ' '
        else:
            separator_position = rule.find(rule_separator)
            self.begin = rule[0]
            self.end = rule[separator_position + len(rule_separator):]

    def __str__(self) -> str:
        return self.begin + rule_separator + self.end

    def __eq__(self, o: object) -> bool:
        return self.begin == o.begin and self.end == o.end


class Grammar:
    def __init__(self) -> None:
        super().__init__()
