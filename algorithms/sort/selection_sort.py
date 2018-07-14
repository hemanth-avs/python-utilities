"""
    Selection Sort
"""


def sort(collection):

    input_len = len(collection)

    for outer_idx in range(input_len):

        lowest_value_index = outer_idx

        for inner_idx in range(outer_idx+1, input_len):
            if collection[lowest_value_index] > collection[inner_idx]:
                lowest_value_index = inner_idx

        collection[lowest_value_index], collection[outer_idx] = collection[outer_idx], collection[lowest_value_index]
