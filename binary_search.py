import random
import time

# binary search
# sorted list
def binarySearch(l, target, low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return target
    elif target < l[midpoint]:
        return binarySearch(l, target, low, midpoint - 1)
    else:
        return binarySearch(l, target, midpoint + 1, high)


if __name__ == "__main__":

    length = 10000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list():
        binarySearch(sorted_list, target)
    end = time.time()
    print("Binary Search time: ", (end - start) / length, "seconds")
