import time
import timeit
import matplotlib.pyplot as plt
import random

# merge sort source:  https://www.geeksforgeeks.org/merge-sort/
def merge_sort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # Into 2 halves
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# insertion sort source: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertion_sort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position

def measure_time(algorithm, arr):
    # Perform multiple iterations for accurate measurement
    time_taken = timeit.timeit(lambda: algorithm(arr.copy()), number=100)
    return time_taken / 100  # Average time per iteration

def generate_data(input_sizes):
    merge_sort_times = []
    insertion_sort_times = []

    for size in input_sizes:
        merge_times = []
        insertion_times = []
        for _ in range(30):  # 30 trials for each input size
            arr = [random.randint(0, 1000) for _ in range(size)]

            # Measure time for Merge sort
            merge_time = measure_time(merge_sort, arr)
            merge_times.append(merge_time)

            # Measure time for Insertion sort
            insertion_time = measure_time(insertion_sort, arr)
            insertion_times.append(insertion_time)

        # Average times over 30 trials
        avg_merge_time = sum(merge_times) / len(merge_times)
        avg_insertion_time = sum(insertion_times) / len(insertion_times)

        merge_sort_times.append(avg_merge_time)
        insertion_sort_times.append(avg_insertion_time)

        print(
            f"Input Size: {size}, Merge Sort Time: {avg_merge_time:.6f} seconds, Insertion Sort Time: {avg_insertion_time:.6f} seconds")

    return merge_sort_times, insertion_sort_times


def plot_results(input_sizes, merge_sort_times, insertion_sort_times):
    plt.plot(input_sizes, merge_sort_times, label='Merge Sort')
    plt.plot(input_sizes, insertion_sort_times, label='Insertion Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Merge Sort vs Insertion Sort')
    plt.legend()
    plt.grid(True)
    plt.show()

# Experiment setup
# input_sizes = [10, 100, 500, 1000, 2000, 5000, 10000]
input_sizes = list(range(60, 70))
merge_sort_times, insertion_sort_times = generate_data(input_sizes)

# Results
plot_results(input_sizes, merge_sort_times, insertion_sort_times)
