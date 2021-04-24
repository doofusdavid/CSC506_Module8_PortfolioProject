import numpy as np
import timeit
import mergesort
import quicksort
import radixsort
import revised_quicksort
import shellsort
import insertionsort
import math

LIST_SIZE = 500
MAX_VALUE = 999
NUM_ITERATIONS = 20


def mergesort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    mergesort.merge_sort(numbers, 0, len(numbers)-1)


def quicksort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    quicksort.quicksort(numbers, 0, len(numbers)-1)


def radixsort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    radixsort.radix_sort(numbers)


def revised_quicksort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    revised_quicksort.revised_quicksort(numbers, 0, len(numbers)-1, 100)


def shellsort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    shellsort.shell_sort(numbers, get_shellsort_gaps())


def timsort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    numbers.sort()


def insertionsort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    insertionsort.insertion_sort(numbers)


def get_shellsort_gaps():
    max_val = int(math.log(LIST_SIZE, 2))
    gaps = []
    for i in range(max_val, 0, -1):
        gaps.append((2**i)-1)
    return gaps


def perform_test():
    results = {}
    results["Insertion Sort"] = timeit.timeit(
        lambda: insertionsort_test(), number=NUM_ITERATIONS)
    results["Merge Sort"] = timeit.timeit(
        lambda: mergesort_test(), number=NUM_ITERATIONS)
    results["Quick Sort"] = timeit.timeit(
        lambda: quicksort_test(), number=NUM_ITERATIONS)
    results["Radix Sort"] = timeit.timeit(
        lambda: radixsort_test(), number=NUM_ITERATIONS)
    results["Revised Quicksort"] = timeit.timeit(
        lambda: revised_quicksort_test(), number=NUM_ITERATIONS)
    results["Shell Sort"] = timeit.timeit(
        lambda: shellsort_test(), number=NUM_ITERATIONS)
    results["Tim Sort"] = timeit.timeit(
        lambda: timsort_test(), number=NUM_ITERATIONS)

    sorted_results = sorted(results.items(), key=lambda x: x[1])

    print("{:<21} | {:>9}".format("List size:", LIST_SIZE))
    print("{:<21} | {:>9}".format("Maximum Int Value:", MAX_VALUE))
    print("{:<21} | {:>9}".format("Sorts per algorithm:", NUM_ITERATIONS))

    print("-"*33)
    print("|{:<20} |{:<10}".format("Sorting Method", "Time"))
    print("-"*33)
    for item in sorted_results:
        print("|{:<20} |{:<10.8f}".format(item[0], item[1]))


perform_test()
