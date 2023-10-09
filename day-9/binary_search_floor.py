def binary_search_floor(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left+(right - left)
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            floor = arr[mid]
            left = mid+1
        else:
            ceil = arr[mid]
            right = mid-1
    return ceil


arr = [1, 2, 8, 10, 10, 12, 19]
t = 7
print(binary_search_floor(arr, t))
