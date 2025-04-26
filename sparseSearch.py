def search_string(arr, x):
    # T: O(log n), S: O(log n)
    def binary_search(arr, x, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        # Move mid to the closest non-empty string
        if arr[mid] == "":
            left = mid - 1
            right = mid + 1
            while True:
                if left < low and right > high:
                    return -1
                if left >= low and arr[left] != "":
                    mid = left
                    break
                if right <= high and arr[right] != "":
                    mid = right
                    break
                left -= 1
                right += 1

        # Standard binary search comparison
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, x, mid + 1, high)
        else:
            return binary_search(arr, x, low, mid - 1)

    return binary_search(arr, x, 0, len(arr) - 1)
