from unittest import TestCase, main
from wk3d4_arr import arr_zero 

class ZeroTest(TestCase):
    
    def test_1_arr1(self):
        self.assertEqual(arr_zero([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_2_arr2(self):
        self.assertEqual(arr_zero([1, 7, 0, 0, 8, 0, 10, 12, 0, 4]), [1, 7, 8, 10, 12, 4, 0, 0, 0, 0])


if __name__ == "__main__":
        main()
