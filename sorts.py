import random


def bubble_sort(unsorted_list: list) -> list:
    """
    Sorts a list littlest to biggest
    :param unsorted_list: An unsorted list
    :return: A sorted list
    >>> bubble_sort(random.sample(range(10), 10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i, _ in enumerate(unsorted_list):
        swap = False
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
                swap = True
        if not swap:
            break
    return unsorted_list


def split(lyst: list) -> (list, list):
    """
    Splits a list and returns the halves
    :param lyst: a list to splilt
    :return: left/right list
    >>> split(list(range(7)))
    ([0, 1, 2], [3, 4, 5, 6])
    """
    half = len(lyst)//2
    return lyst[:half], lyst[half:]


def merge(first: list, second: list) -> list:
    """
    Merge two lists together by picking the smallest item from each list,
    left to right.
    :param first: one list
    :param second: another list
    :return: merge of first and second
    >>> merge(list(range(5, 10)), list(range(7, 15)))
    [5, 6, 7, 7, 8, 8, 9, 9, 10, 11, 12, 13, 14]
    """
    unsorted_list = list(range(len(first) + len(second)))
    i = j = k = 0
    while i < len(first) and j < len(second):
        left_item = first[i]
        right_item = second[j]
        if left_item < right_item:
            unsorted_list[k] = left_item
            i += 1
        else:
            unsorted_list[k] = right_item
            j += 1
        k += 1
    while i < len(first):
        unsorted_list[k] = first[i]
        k += 1
        i += 1
    while j < len(second):
        unsorted_list[k] = second[j]
        k += 1
        j += 1
    return unsorted_list


def merge_sort(unsorted_list: list) -> list:
    """
    Sorts an unsorted list, smallest to largest
    :param unsorted_list: A list that needs sorting
    :return: A list that doesn't need sorting
    >>> merge_sort(random.sample(range(10), 10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(unsorted_list) <= 1:
        return unsorted_list
    left, right = split(unsorted_list)
    sort_left = merge_sort(left)
    sort_right = merge_sort(right)
    return merge(sort_left, sort_right)


def insertion_sort(unsorted_list):
    """

    :param unsorted_list:
    :return:
    >>> insertion_sort(random.sample(range(10), 10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    i = 1
    while i < len(unsorted_list):
        j = i
        while j > 0:
            if unsorted_list[j-1] > unsorted_list[j]:
                unsorted_list[j - 1], unsorted_list[j] = unsorted_list[j], \
                                                         unsorted_list[j - 1]
            else:
                break
            j -= 1
        i += 1
    return unsorted_list

