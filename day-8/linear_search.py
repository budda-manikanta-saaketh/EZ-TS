def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

n = int(input())
li = list(map(int, input().split(",")))[:n]
x = int(input())
result = linear_search(li, x)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
