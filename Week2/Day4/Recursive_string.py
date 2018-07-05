import unittest
def get_permutations(string):
    l=0
    s=set()
    r=len(string)-1
    if(len(string)==0):
        s.add(string)
        return s
    permutation(list(string),l,r,s)
    return s
    
def toString(List):
    return ''.join(List)
     
    
def permutation(array, l,r,s):
    if l==r:
        k=toString(array)
        s.add(k)
    else:
        for i in range(l,r+1):
            temp=array[l]
            array[l]=array[i]
            array[i]=temp
            permutation(array, l+1, r,s)
            
            array[l],array[i] = array[i], array[l] 
    

    return s
# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)