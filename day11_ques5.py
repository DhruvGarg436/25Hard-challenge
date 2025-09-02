from enum import Enum


class ABC(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5


for i in range(5, 0, -1):
    for j in range(6-i):
        print(str(ABC(i)).replace("ABC.", ""), end=" ")
        i += 1
    print()
