def sliding_window(arr, k):
    n = len(arr)
    if k > n:
        return []
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)
    return max_sum
arr = [1, 2, 3, 4, 5]
k = 3
print(sliding_window(arr, k))