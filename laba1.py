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

 
           
