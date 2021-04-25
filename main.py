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

LIST_SIZE = 50000
MAX_VALUE = sys.maxsize
NUM_ITERATIONS = 20
word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()
LIST_TYPE = "integer"


def get_list():
    if LIST_TYPE == "integer":
        return list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    elif LIST_TYPE == "float":
        return list(np.random.random(size=LIST_SIZE))
    elif LIST_TYPE == "string":
        return list(np.random.choice(WORDS, size=5))


def mergesort_test():
    sort_list = get_list()
    mergesort.merge_sort(sort_list, 0, len(sort_list)-1)


def quicksort_test():
    sort_list = get_list()
    quicksort.quicksort(sort_list, 0, len(sort_list)-1)


def revised_quicksort_test():
    sort_list = get_list()
    revised_quicksort.revised_quicksort(sort_list, 0, len(sort_list)-1, 100)


def shellsort_test():
    sort_list = get_list()
    shellsort.shell_sort(sort_list, get_shellsort_gaps())


def insertionsort_test():
    sort_list = list(np.random.randint(low=1, high=MAX_VALUE, size=LIST_SIZE))
    insertionsort.insertion_sort(sort_list)


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
