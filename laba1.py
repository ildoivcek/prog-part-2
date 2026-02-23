import unittest


def longest_peak(array):
    max_length = 0

    for i in range(1, len(array) - 1):
        if array [i - 1] < array[i] and array[i] > array[i + 1]:
            left_idx = i - 1
            while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
                left_idx -= 1

            right_idx = i + 1
            while right_idx < len(array) and array[right_idx] < array[right_idx - 1]:
                right_idx += 1

            current_length = right_idx - left_idx - 1

            if current_length > max_length:
                max_length = current_length

    return max_length

class TestLongestPeak(unittest.TestCase):

    def test_example(self):
        self.assertEqual(longest_peak([1, 3, 5, 4, 2, 8, 3, 7]), 5)

    def test_sorted_zrostae(self):
        self.assertEqual(longest_peak([1, 2, 3, 4, 5]), 0)

    def test_sorted_spadae(self):
        self.assertEqual(longest_peak([5, 4, 3, 2, 1,]), 0)

    def test_two_elements(self):
        self.assertEqual(longest_peak([1, 2]), 0)

    def test_no_peaks(self):
        self.assertEqual(longest_peak([2, 2, 2]), 0)
        self.assertEqual(longest_peak([-1, -5, -1]), 0)

    def test_three_peaks(self):
        self.assertEqual(longest_peak([1, 3, 2, 1, 5, 4, 1, 4, 8, 6, 2]), 5)


if __name__ == '__main__':
    unittest.main()
           

 
           
