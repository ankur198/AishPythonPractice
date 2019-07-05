a = [1, 2, 4, 35, 45, 88, 103, 108]
tofind = 88


def binary(start, end, toFind):
    midIndex = (start+end)//2
    if start == end-1:
        return -1
    if a[midIndex] == toFind:
        return midIndex
    elif a[midIndex] < toFind:
        return binary(midIndex, end, toFind)
    else:
        return binary(start, midIndex, toFind)


print(binary(0, len(a), 6))