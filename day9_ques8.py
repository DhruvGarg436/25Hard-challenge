for i in range(1, 6):
    if i == 1 or i == 2:
        print(" "*(5-i), end="")
        print("* "*i)
    else:
        print(" "*(5-i), end="")
        print("*", " "*(i*2-5), "*")

for i in range(4, 0, -1):
    if i == 4 or i == 3:
        print(" "*(5-i), end="")
        print("*", " "*(i*2-5), "*")
    else:
        print(" "*(5-i), end="")
        print("* "*i)
