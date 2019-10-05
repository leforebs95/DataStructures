from collections import deque


def split(list0):
    half = len(list0)//2
    list1 = list0[:half]
    list2 = list0[half:]
    return list1, list2


def merge(unsorted, list1: list, list2: list):

    if




    print(unsorted, list1, list2)
    deq1 = deque(list1)
    deq2 = deque(list2)
    sort_list = []
    for i, left in enumerate(list1):
        for j, right in enumerate(list2):
            print("i: {} j: {} left: {} right: {}".format(i, j, left, right))
            if left < right:
                unsorted[i] = left
            elif right < left:
                unsorted[j] = right
    print(unsorted)

    # print(deq1, deq2)
    if deq1:
        sort_list.extend(deq1)
    elif deq2:
        sort_list.extend(deq2)
    print(sort_list)
    list1 = sort_list
    return unsorted


def merge_sort(unsorted_list):
    print("INput: {}".format(unsorted_list))
    if len(unsorted_list) <= 1:
        return unsorted_list
    left, right = split(unsorted_list)
    left_lyst = merge_sort(left)
    right_lyst = merge_sort(right)
    return merge(unsorted_list, left_lyst, right_lyst)


if __name__ == '__main__':
    print(merge_sort([6, 7, 1, 2, 5, 0, 2, 3, 6, 2, 7, 8, 3, 4]))
