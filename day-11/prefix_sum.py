def prefix_sum(arr):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        if i==0:
            prefix_sum[i]=arr[i]
            continue
        prefix_sum[i] = arr[i] + arr[i-1]
    return prefix_sum
arr = [1, 2, 3, 4, 5]
prefix_sum_arr = prefix_sum(arr)
print(prefix_sum_arr)
