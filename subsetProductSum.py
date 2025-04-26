# T: O(n), S: O(1)
def subsetProductSum(arr):
    result = 1
    for num in arr:
        result *= num + 1
    return result - 1


# Example
arr = [1, 2, 3]
print(subsetProductSum(arr))  # Output: 23
