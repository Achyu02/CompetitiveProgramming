import unittest


def find_duplicate(list):
    n = len(list)
    first = n
    last = n
    while True:
        first = list[first - 1] 
        last = list[last - 1] 
        last = list[last - 1]
        if first == last:
            break
    last = n
    while True:
        first = list[first - 1]
        last = list[last - 1]
        if first == last:
            break
    return first

# Tests

class Test(unittest.TestCase):
    
    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)
    
    def test_short(self):
        actual = find_duplicate([2, 3, 1, 3])
        expected = 3
        self.assertEqual(actual, expected)


    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)