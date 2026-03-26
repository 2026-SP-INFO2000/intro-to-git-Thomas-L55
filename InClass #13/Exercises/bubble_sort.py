def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


# Test the function
nums = [5, 2, 9, 1, 5, 6]
print("Original list:", nums)
print("Sorted list:", bubble_sort(nums))