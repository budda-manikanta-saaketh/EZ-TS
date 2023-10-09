def TOH(n, src, aux, dest):
    if n <= 1:
        print(src + " -> " + dest)
        return
    TOH(n-1, 'src', 'dest', 'aux')
    print(src + " -> " + dest)
    TOH(n-1, 'aux', 'src', 'dest')
n = int(input("enter no of disks:"))
TOH(n, 'src', 'aux', 'dest')