import time
import random
import numpy as np

# Sorting algorithms
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Generate datasets
def generate_data(size):
    random_data = [random.randint(1, 10000) for _ in range(size)]
    return random_data

# Measure time for sorting algorithm
def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data.copy())  # Use a copy to avoid modifying original data
    end_time = time.time()
    return end_time - start_time

# Perform trials and compute mean and std deviation
def run_trials(sort_function, size, trials=10):
    times = []
    for _ in range(trials):
        data = generate_data(size)
        time_taken = measure_time(sort_function, data)
        times.append(time_taken)
    mean_time = np.mean(times)
    std_time = np.std(times)
    return mean_time, std_time

# Compare algorithms on different datasets
def compare_algorithms(sizes, trials=10):
    for size in sizes:
        print(f"Dataset size: {size}")

        # Merge Sort
        merge_mean, merge_std = run_trials(merge_sort, size, trials)
        print(f"Merge Sort: Mean Time = {merge_mean:.6f} seconds, Std Dev = {merge_std:.6f} seconds")

        # Bubble Sort
        bubble_mean, bubble_std = run_trials(bubble_sort, size, trials)
        print(f"Bubble Sort: Mean Time = {bubble_mean:.6f} seconds, Std Dev = {bubble_std:.6f} seconds")

        # Radix Sort
        radix_mean, radix_std = run_trials(radix_sort, size, trials)
        print(f"Radix Sort: Mean Time = {radix_mean:.6f} seconds, Std Dev = {radix_std:.6f} seconds")

        print()  # Add a new line for readability

# Dataset sizes to compare
sizes = [100, 500, 1000, 1000000]

# Run the comparisons
compare_algorithms(sizes)