import unittest
import main

class TestSum(unittest.TestCase):
    def test_sum_correct(self):
        self.assertEqual(main.sum(5, 5), 10, "Erreur: fonction sum")

    def test_sum_incorrect(self):
        self.assertEqual(main.sum(5, 5), 9, "Erreur: fonction sum")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSum))

    result = unittest.TestResult()

    suite.run(result)

    if len(result.failures) > 0:
        print("Liste des tests échoués :")
        for test, traceback in result.failures:
            print(test)
    
    unittest.main()
