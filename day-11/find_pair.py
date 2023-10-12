# given a list in which if a pair exists whose sum is equal to target print the pair
l = list(map(int,input().split(" ")))
target = int(input())
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] + l[j] == target:
            print(l[i], l[j])
            break
    else:
        continue
    break
else:
    print("no pair found")
