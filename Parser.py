from Grammar import Rule


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