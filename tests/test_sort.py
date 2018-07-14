import unittest
import random
from algorithms.sort import bubble_sort


def generate_random_array(cnt):
    random_list = []
    for index in range(cnt):
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


if __name__ == "__main__":
    unittest.main()
