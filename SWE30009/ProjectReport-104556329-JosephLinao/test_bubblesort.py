import unittest
from downloads00000062 import bubblesort

class TestBubbleSort(unittest.TestCase):
    # MR1: Reversing the input
    def test_mtg1_sort_normal_and_reverse(self):
        normal_list = [3, 1, 4, 1, 5]
        reverse_list = list(reversed(normal_list))
        self.assertEqual(bubblesort(normal_list), bubblesort(reverse_list))
    def test_mtg2_sort_repeated_elements_and_reverse(self):
        normal_list = [5, 2, 2, 8]
        reverse_list = list(reversed(normal_list))
        self.assertEqual(bubblesort(normal_list), bubblesort(reverse_list))
    def test_mtg3_sort_already_sorted_and_reverse(self):
        normal_list = [1, 2, 3, 4]
        reverse_list = list(reversed(normal_list))
        self.assertEqual(bubblesort(normal_list), bubblesort(reverse_list))
    def test_mtg4__sort_negative_positive_and_reverse(self):
        normal_list = [-3, 0, 2, 1]
        reverse_list = list(reversed(normal_list))
        self.assertEqual(bubblesort(normal_list), bubblesort(reverse_list))
    def test_mtg5_sort_long_random_list_and_reverse(self):
        normal_list = [9, 7, 5, 3, 1]
        reverse_list = list(reversed(normal_list))
        self.assertEqual(bubblesort(normal_list), bubblesort(reverse_list))
    # MR2: Concatenation of Sorted Lists
    def test_mtg6_concatenate_two_small_sorted_lists(self):
        list_1 = [1, 3]
        list_2 = [2, 4]
        concatenated_list = list_1 + list_2
        sorted_concatenated_list = bubblesort(concatenated_list)
        merged_sorted_list = bubblesort(list_1 + list_2)
        self.assertEqual(sorted_concatenated_list, merged_sorted_list)
    def test_mtg7_concatenate_two_large_sorted_lists(self):
        list_1 = [1, 3, 5, 7]
        list_2 = [2, 4, 6, 8]
        concatenated_list = list_1 + list_2
        sorted_concatenated_list = bubblesort(concatenated_list)
        merged_sorted_list = bubblesort(list_1 + list_2)
        self.assertEqual(sorted_concatenated_list, merged_sorted_list)
    def test_mtg8_concatenate_repeated_elements_and_sort(self):
        list_1 = [2, 2, 5]
        list_2 = [5, 7, 7]
        concatenated_list = list_1 + list_2
        sorted_concatenated_list = bubblesort(concatenated_list)
        merged_sorted_list = bubblesort(list_1 + list_2)
        self.assertEqual(sorted_concatenated_list, merged_sorted_list)
    def test_mtg9_concatenate_negative_positive_lists(self):
        list_1 = [-5, -3, 1]
        list_2 = [2, 4, 6]
        concatenated_list = list_1 + list_2
        sorted_concatenated_list = bubblesort(concatenated_list)
        merged_sorted_list = bubblesort(list_1 + list_2)
        self.assertEqual(sorted_concatenated_list, merged_sorted_list)
    def test_mtg10_concatenate_sorted_unsorted_list(self):
        list_1 = [1, 3, 5]
        list_2 = [7, 2, 6]
        concatenated_list = list_1 + list_2
        sorted_concatenated_list = bubblesort(concatenated_list)
        merged_sorted_list = bubblesort(list_1 + list_2)
        self.assertEqual(sorted_concatenated_list, merged_sorted_list)

if __name__ == "__main__":
    unittest.main()