def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Test the function
nums = [1, 2, 3, 4, 5, 6, 7, 8]
target = 5

result = binary_search(nums, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")