def pascal_triangle(n):
    for j in range(n):
        print(" " * (n - j), end="")
        num = 1
        for i in range(j + 1):
            print(num, end=" ")
            num = num * (j - i) // (i + 1)
        print()


pascal_triangle(5)
