count = 0
for i in range(5):
    for j in range(i+1):
        if count % 2 == 0:
            print(chr(97+count), end=" ")
            count += 1
        else:
            print(chr(65+count), end=" ")
            count += 1
    print()
