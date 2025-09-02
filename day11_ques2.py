for i in range(5):
    if i % 2 == 0:
        tem = True
        for j in range(i+1):
            if tem == True:
                print(1, end=" ")
            else:
                print(0, end=" ")
            tem = not (tem)
        print()
    else:
        tem = False
        for j in range(i+1):
            if tem == True:
                print(1, end=" ")
            else:
                print(0, end=" ")
            tem = not (tem)
        print()
