def gen_magic_square(n):
    
    magic_square = [[0] * n for _ in range(n)]
    row, col = 0, n // 2
    num = 1

    while num <= n * n:
        magic_square[row][col] = num
        num += 1
        new_row, new_col = (row - 1) % n, (col + 1) % n

        if magic_square[new_row][new_col] != 0:
            row = (row + 1) % n
        else:
            row, col = new_row, new_col

    return magic_square

def print_(magic_square):
    for row in magic_square:
        for num in row:
            print(num, end="\t")
        print()

try:
    n = int(input("Enter an odd integer for the order of the magic square: "))
    magic_square = gen_magic_square(n)
    print("Magic Square of Order", n, "is:")
    print_(magic_square)
except ValueError as e:
    print(e)