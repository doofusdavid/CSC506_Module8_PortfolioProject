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
import pandas as pd

LIST_SIZE = 50000
MAX_VALUE = sys.maxsize
NUM_ITERATIONS = 20
word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()
LIST_TYPE = "integer"


def get_list(list_type, list_size):
    if list_type == "integer":
        return list(np.random.randint(low=1, high=MAX_VALUE, size=list_size))
    elif list_type == "float":
        return list(np.random.random(size=list_size))
    elif list_type == "string":
        return list(np.random.choice(WORDS, size=list_size))


def run_single_test(algorithm, list_type, list_size):
    sort_list = get_list(list_type, list_size)

    pr = cProfile.Profile()
    pr.enable()
    if algorithm == "merge_sort":
        mergesort.merge_sort(sort_list, 0, len(sort_list)-1)
    elif algorithm == "quicksort":
        quicksort.quick_sort(sort_list, 0, len(sort_list)-1)
    elif algorithm == "revised_quicksort":
        revised_quicksort.revised_quicksort(
            sort_list, 0, len(sort_list)-1, 50)
    elif algorithm == "shell_sort":
        shellsort.shell_sort(sort_list, get_shellsort_gaps(list_size))

    pr.disable()

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.strip_dirs().print_stats()

    results = s.getvalue()
    for line in results.splitlines():
        if "_sort" in line:
            split_line = line.strip().split("    ")
            return(split_line[3])


def get_shellsort_gaps(list_size):
    max_val = int(math.log(list_size, 2))
    gaps = []
    for i in range(max_val, 0, -1):
        gaps.append((2**i)-1)
    return gaps


def run_tests():
    results = []
    for algorithm in ["merge_sort", "quicksort", "revised_quicksort", "shell_sort"]:
        for list_type in ["integer", "float", "string"]:
            for list_size in [100, 1000, 10000]:
                time = run_single_test(algorithm, list_type, list_size)
                results.append([algorithm,  list_type, list_size, time])

    df = pd.DataFrame(results, columns=[
                      "Algorithm", "List_Type", "List_Size", "Time"])
    df.to_csv("test_results.csv")


# print(run_single_test("merge_sort", "integer", 1000))

run_tests()

# pr = cProfile.Profile()
# pr.enable()
# performtests()
# pr.disable()

# s = io.StringIO()
# ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
# ps.strip_dirs().print_stats()

# results = s.getvalue()
# for line in results.splitlines():
#     if "_test" in line:
#         print(line)


# value = cProfile.run('shellsort_test()')
# print(value)
