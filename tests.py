import unittest

from Grammar import Rule


class RuleTests(unittest.TestCase):
    rule1_representation = "S->aTc|bSc"
    rule1 = Rule(rule1_representation)
    rule1_copy = Rule(rule1_representation)

    rule2_representation = "S->aTb|aSa"
    rule2 = Rule(rule2_representation)

    def testStringConversion(self):
        self.assertEqual(str(self.rule1), self.rule1_representation)

    def testEquality(self):
        self.assertEqual(self.rule1, self.rule1)
        self.assertNotEqual(self.rule1, self.rule2)


if __name__ == '__main__':
    unittest.main()
