n = 4
size = 2 * n - 1   # 7 for n=4

for i in range(size):
    for j in range(size):
        # distance from top
        top = i
        # distance from left
        left = j
        # distance from bottom
        bottom = size - 1 - i
        # distance from right
        right = size - 1 - j

        # find the minimum distance from any edge
        if top < left:
            min1 = top
        else:
            min1 = left

        if bottom < right:
            min2 = bottom
        else:
            min2 = right

        if min1 < min2:
            min_dist = min1
        else:
            min_dist = min2

        # value decreases with layer depth
        print(n - min_dist, end=" ")
    print()
