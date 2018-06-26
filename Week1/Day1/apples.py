def get_maximum(stock_prices):

    if len(stock_prices) < 2:
        raise ValueError('Minimum of 2 prices')

    minimum  = stock_prices[0]
    maximum = stock_prices[1] - stock_prices[0]
    for i in xrange(1, len(stock_prices)):
        present = stock_prices[i]
        profit = present - minimum

        maximum = max(maximum, profit)

    
        minimum  = min(minimum, present)

    return maximum


# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_maximum([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_maximum([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_maximum([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_maximum([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_maximum([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            get_maximum([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            get_maximum([])

unittest.main(verbosity=2)
