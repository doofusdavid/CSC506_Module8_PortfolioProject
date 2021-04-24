def insertion_sort_interleaved(numbers, start_index, gap):
    swaps = 0
    for i in range(start_index + gap, len(numbers), gap):
        j = i
        while (j - gap >= start_index) and (numbers[j] < numbers[j - gap]):
            swaps += 1
            temp = numbers[j]
            numbers[j] = numbers[j - gap]
            numbers[j - gap] = temp
            j = j - gap
    return swaps


def shell_sort(numbers, gap_values):
    swaps = []
    for gap_value in gap_values:
        for i in range(gap_value):
            swaps.append(insertion_sort_interleaved(numbers, i, gap_value))
    return swaps
