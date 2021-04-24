def slice_insertion_sort(num_list, start, end):
    for i in range(start+1, end+1):
        val = num_list[i]
        j = i
        while j > start and num_list[j-1] > val:
            num_list[j] = num_list[j-1]
            j -= 1
        num_list[j] = val


def partition(numbers, start_index, end_index):
    # Select the middle value as the pivot.
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]

    # "low" and "high" start at the ends of the list segment
    # and move towards each other.
    low = start_index
    high = end_index

    done = False
    while not done:
        # Increment low while numbers[low] < pivot
        while numbers[low] < pivot:
            low = low + 1

        # Decrement high while pivot < numbers[high]
        while pivot < numbers[high]:
            high = high - 1

        # If low and high have crossed each other, the loop
        # is done. If not, the elements are swapped, low is
        # incremented and high is decremented.
        if low >= high:
            done = True
        else:
            temp = numbers[low]
            numbers[low] = numbers[high]
            numbers[high] = temp
            low = low + 1
            high = high - 1

    # "high" is the last index in the left segment.
    return high


def revised_quicksort(numbers, start_index, end_index, threshold):
    # Only attempt to sort the list segment if there are
    # at least 2 elements
    if end_index <= start_index:
        return
    if end_index - start_index <= threshold:
        slice_insertion_sort(numbers, start_index, end_index)
        return
    # Partition the list segment
    high = partition(numbers, start_index, end_index)

    # Recursively sort the left segment
    revised_quicksort(numbers, start_index, high, threshold)

    # Recursively sort the right segment
    revised_quicksort(numbers, high + 1, end_index, threshold)