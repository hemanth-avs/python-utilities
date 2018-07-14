"""
Bubble Sort
"""


def sort(collection):

    collection_len = len(collection)

    for outer_idx in range(collection_len):
        is_sorted = True
        for inner_idx in range(collection_len-outer_idx-1):
            if collection[inner_idx] > collection[inner_idx+1]:
                collection[inner_idx], collection[inner_idx+1] = collection[inner_idx+1], collection[inner_idx]
                is_sorted = False
        if is_sorted:
            break
