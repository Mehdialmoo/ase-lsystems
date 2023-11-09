import unittest
from lsystem import LSystem

class TestLSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.iterations = 2
        self.lsystem = LSystem()
        
    def test_replacement_rules1(self):
        rules = { 'a' : 'b', 'b' : 'a' }
        state = "aba"
        self.lsystem.set_rules(rules)

        for _ in range (self.iterations):
            state = self.lsystem.generate_next_state(state)
        
        self.assertEqual(state , "aba")


if __name__ == "__main__":
    unittest.main()