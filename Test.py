import unittest
import main

# test
class TestSum(unittest.TestCase):
    def testsum(self):
        self.assertEqual(main.sum(5, 5), 10, "Erreur: fonction sum")
        self.assertEqual(main.sum(4, 5), 2, "Erreur: fonction sum")
        self.assertEqual(main.sum(51, -50), 1, "Erreur: fonction sum")
        self.assertEqual(main.sum(1, 8), 7, "Erreur: fonction sum")


unittest.main()