import unittest
import selection_sort

class test_selection_sort(unittest.TestCase):
    def test_1(self):
        self.assertEqual(selection_sort.selection_sort([9, 1, 3, 5, 7, 8, 2, 4, 6, 6, 6]),[1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9])

    def test_2(self):
        self.assertEqual(selection_sort.selection_sort([4, 1, 3, 2]),[1, 2, 3, 4])

    def test_3(self):
        self.assertEqual(selection_sort.selection_sort([9, 1, 3, 5,44,11,55, 7, 8, 2, 4, 6, 6, 6]),[1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9,11,44,55])

    def test_4(self):
        self.assertEqual(selection_sort.selection_sort([4, 1, 3, 2], asc=False),[4, 3, 2, 1])

    def test_5(self):
        self.assertEqual(selection_sort.selection_sort([9, 1, 3, 5, 7, 8, 2, 4, 6, 6, 6], asc=False),[9, 8, 7, 6, 6, 6, 5, 4, 3, 2, 1])

if __name__=="__main__":
    unittest.main()