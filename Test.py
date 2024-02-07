import unittest
import main

# test
class TestSum(unittest.TestCase):
    def testsum(self):
        self.assertEqual(main.sum(5, 5), 10, "Erreur: fonction sum")


unittest.main()