import xmlrunner
import unittest
import main

class TestSum(unittest.TestCase):
    def test_sum_correct(self):
        self.assertEqual(main.sum(5, 5), 10, "Erreur: fonction sum")

    def test_sum_incorrect(self):
        self.assertEqual(main.sum(5, 5), 9, "Erreur: fonction sum")

suite = unittest.TestLoader().loadTestsFromTestCase(TestSum)
runner = xmlrunner.XMLTestRunner(output='test-reports')
runner.run(suite)
unittest.main()