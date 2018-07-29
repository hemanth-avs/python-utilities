"""
    Insertion Sort
"""


def sort(collection):
    """
    Insetion sort
    :param collection: Input Array
    """
    for outer_ind in range(1, len(collection)):
        for inner_idx in range(outer_ind, 0, -1):
            if collection[inner_idx] < collection[inner_idx-1]:
                collection[inner_idx], collection[inner_idx - 1] = collection[inner_idx - 1], \
                                                                   collection[inner_idx]
            else:
                break
