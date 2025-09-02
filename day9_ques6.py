for i in range(1, 6):
    if i == 3 or i == 4:
        print(" "*(5-i), end="")
        print("*", " "*(i*2-5), "*")
    else:
        print(" "*(5-i), end="")
        print("* "*i)
