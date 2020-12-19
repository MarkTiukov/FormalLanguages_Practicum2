import unittest

from Grammar import Rule, Grammar
from Parser import Situation


class RuleTests(unittest.TestCase):
    rule1_representation = "S->aTc|bSc"
    rule1 = Rule(rule1_representation)
    rule1_copy = Rule(rule1_representation)

    rule2_representation = "S->aTb|aSa"
    rule2 = Rule(rule2_representation)

    def testStringConversion(self):
        self.assertEqual(str(self.rule1), self.rule1_representation)

    def testEquality(self):
        self.assertTrue(self.rule1 == self.rule1)
        self.assertFalse(self.rule1 == self.rule2)


class GrammarTests(unittest.TestCase):
    alphabet = {'(', ')'}

    initiative_rule_representation = "U->S"
    initiative_rule = Rule(initiative_rule_representation)

    left_rule_representation = "S->(S)S"
    left_rule = Rule(left_rule_representation)

    right_rule_representation = "S->S(S)"
    right_rule = Rule(right_rule_representation)

    concatenation_rule_representation = "S->SS"
    concatenation_rule = Rule(concatenation_rule_representation)

    ending_rule_representation = "S->"
    ending_rule = Rule(ending_rule_representation)

    grammar1 = Grammar(rules=[initiative_rule], alphabet=alphabet)
    grammar2 = Grammar(rules=[initiative_rule, left_rule])
    full_grammar = Grammar(rules=[initiative_rule,
                                  left_rule,
                                  right_rule,
                                  ending_rule],
                           alphabet=alphabet)

    def testAddRule(self):
        self.grammar1.addRule(self.left_rule)
        self.assertEqual(self.grammar1, self.grammar2)
        self.grammar1.addRule(self.right_rule)
        self.grammar1.addRule(self.ending_rule)
        self.assertEqual(self.grammar1, self.full_grammar)

    def testGetRule(self):
        result = [self.left_rule, self.right_rule, self.ending_rule]
        self.assertEqual(self.full_grammar.getRule('S'), result)


class SituationTests(unittest.TestCase):
    rule = Rule("S->S(S)")
    situation1 = Situation(rule, 4, 2)
    situation2 = Situation(rule, 3, 2)
    situation3 = Situation(rule, 2, 2)
    situation3_copy = Situation(rule, 2, 2)

    situation4 = Situation(Rule("S->"), 0, 0)

    def testIsCompleted(self):
        self.assertTrue(self.situation1.isCompleted())
        self.assertFalse(self.situation2.isCompleted())

    def testGetCurrentSymbol(self):
        self.assertEqual(self.situation1.getCurrentSymbol(), '')
        self.assertEqual(self.situation2.getCurrentSymbol(), ')')
        self.assertEqual(self.situation3.getCurrentSymbol(), 'S')

    def testEquality(self):
        self.assertTrue(self.situation3 == self.situation3_copy)
        self.assertFalse(self.situation3 == self.situation4)


if __name__ == '__main__':
    unittest.main()
