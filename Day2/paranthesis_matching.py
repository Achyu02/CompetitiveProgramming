import unittest


def get_closing_paren(sentence, start_index):

    open_parameter=0
    pointer=start_index+1
    for pointer in range(start_index+1, len(sentence)):
        char=sentence[pointer]
        if char== '(':
            open_parameter+= 1
        elif char == ')':
            if open_parameter==0:
                return pointer
            else:
                open_parameter-=1
    raise Exception("Invalid operation")


# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)