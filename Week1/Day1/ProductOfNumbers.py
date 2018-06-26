import unittest


def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    if(len(int_list)<2):
        raise Exception("hdd")
    else:
#        print("input",int_list)
#        k=[]
#        for i in range(len(int_list)):
#            temp=1
#            for j in range(len(int_list)):
#                if i==j:
#                    continue
        #         else:
        #             temp=temp*int_list[j]
        #     k.insert(i,temp)
        
        # print("output",k)
    
        # return k
        print("jjjjjjjjjjjjjjj",int_list)
        #a=[1]*len(int_list)
        a=[]
        b=[]
        #b=[1]*len(int_list)
        print(a,"list")
        p=1
        for i in range(len(int_list)):
            a.append(p)
            p=p*int_list[i]
        print(a)
        q=1
        for i in range(len(int_list)-1,-1,-1):
            b.append(q)
            q=q*int_list[i]
        print(b)
        b=b[::-1]
        k=[]
        
        for i in range (len(int_list)):
            k.append(a[i]*b[i])
            
        print(k)
        return k
        
        


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)