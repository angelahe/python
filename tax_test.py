import unittest
from tax import calc_tax

class TestCalcTaxFunction(unittest.TestCase):

    incomes = [(1.00, 0.15),
        (2.0,0.3), 
        (50000,7630.35),
        (100000, 18141.11),
        (150000, 31211.10),
        (250000, 61796.26)]

    def test_calc_tax_no_input(larry):
        larry.assertEqual(calc_tax(), 0)

    def test_calc_tax_all_brackets(larry):
        for case in larry.incomes:
            larry.assertEqual(calc_tax(case[0]), case[1])

if __name__ == '__main__':
    unittest.main()