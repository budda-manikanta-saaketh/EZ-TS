def count_sort(arr):
    count = [0] * (max(arr) + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(1, (max(arr) + 1)):
        count[i] += count[i - 1]
    sr = [0] * len(arr)
    for i in range(len(arr)):
        sr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return sr
li=list(map(int,input().split(" ")))
print(count_sort(li))
