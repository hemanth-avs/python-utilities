"""
    Quick Sort
"""


def sort(collection, start, end):
    """
    Quick Sort
    :param collection: Input Array
    :return: Sorted Array
    """
    if start >= end:
        return

    pivot_index = partition(collection, start, end)
    sort(collection, start, pivot_index)
    sort(collection, pivot_index+1, end)


def partition(collection, start, end):
    """
    Method which partitions the input.
    :param collection: Array Inout Array.
    :param start: Integer  Start Index of Input array.
    :param end: Integer End Index of Input array.
    """
    pivot = collection[end-1]
    pivot_index = start

    for index in range(start, end):
        if collection[index] <= pivot:
            collection[index], collection[pivot_index] = collection[pivot_index], collection[index]
            pivot_index = pivot_index + 1
    return pivot_index - 1
