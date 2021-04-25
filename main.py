import numpy as np
import timeit
import mergesort
import quicksort
import revised_quicksort
import shellsort
import insertionsort
import math
import cProfile
import pstats
import io
import sys

LIST_SIZE = 500
MAX_VALUE = sys.maxsize
NUM_ITERATIONS = 20


def mergesort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    mergesort.merge_sort(numbers, 0, len(numbers)-1)


def quicksort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    quicksort.quicksort(numbers, 0, len(numbers)-1)


def revised_quicksort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    revised_quicksort.revised_quicksort(numbers, 0, len(numbers)-1, 100)


def shellsort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    shellsort.shell_sort(numbers, get_shellsort_gaps())


def insertionsort_test():
    numbers = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    insertionsort.insertion_sort(numbers)


def get_shellsort_gaps():
    max_val = int(math.log(LIST_SIZE, 2))
    gaps = []
    for i in range(max_val, 0, -1):
        gaps.append((2**i)-1)
    return gaps


def performtests():
    insertionsort_test()
    mergesort_test()
    quicksort_test()
    revised_quicksort_test()
    shellsort_test()


pr = cProfile.Profile()
pr.enable()
performtests()
pr.disable()

s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
ps.strip_dirs().print_stats()

results = s.getvalue()
for line in results.splitlines():
    if "_test" in line:
        print(line)


# value = cProfile.run('shellsort_test()')
# print(value)
