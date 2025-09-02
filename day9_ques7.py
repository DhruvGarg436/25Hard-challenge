for i in range(5, 0, -1):
    if i == 4 or i == 3:
        print(" "*(5-i), end="")
        print("*", " "*(i*2-5), "*")
    else:
        print(" "*(5-i), end="")
        print("* "*i)
