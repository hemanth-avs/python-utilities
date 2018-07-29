"""
    Sorting Test Class
"""

import unittest
import random
from algorithms.sort import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort)


def generate_random_array(cnt):
    """
    Generates Array of Random Numbers
    :param cnt: Number of Random Number to be generated
    :return:
    """
    random_list = []
    for _ in range(cnt):
        random_list.append(random.randint(-1000, 1000))
    return random_list


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.testinput_array = [generate_random_array(1000),
                                generate_random_array(2000),
                                generate_random_array(1500),
                                generate_random_array(800),
                                [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

    def test_bubble_sort(self):
        for test_input in self.testinput_array:
            bubble_sort.sort(test_input)
            self.assertEqual(sorted(test_input), test_input)

    def test_selection_sort(self):
        for test_input in self.testinput_array:
            selection_sort.sort(test_input)
            self.assertEqual(sorted(test_input), test_input)

    def test_insertion_sort(self):
        for test_input in self.testinput_array:
            insertion_sort.sort(test_input)
            self.assertEqual(sorted(test_input), test_input)

    def test_merge_sort(self):
        for test_input in self.testinput_array:
            sorted_output = merge_sort.sort(test_input)
            self.assertEqual(sorted(test_input), sorted_output)

    def test_quick_sort(self):
        for test_input in self.testinput_array:
            quick_sort.sort(test_input)
            self.assertEqual(sorted(test_input), test_input)
