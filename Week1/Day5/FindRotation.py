import unittest


def find_rotation_point(words):
    return rotation(words,0,len(words)-1)
    
def rotation(a,low,high):
    if (high < low):
        return 0
 

    if (high == low):
        return low

    mid = low + (high - low)/2; 
    mid = int(mid)

    if (mid < high and a[mid+1] < a[mid]):
        return (mid+1)

    if (mid > low and a[mid] < a[mid - 1]):
        return mid

    if (a[high] > a[mid]):
        return rotation(a, low, mid-1);
 
    return rotation(a, mid+1, high)

# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)