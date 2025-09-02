for i in range(5):
    print(" "*(8-2*(i)), end="")
    for j in range(i+1, 0, -1):
        print(j, end=" ")
    for j in range(i):
        print(j+2, end=" ")
    print()
