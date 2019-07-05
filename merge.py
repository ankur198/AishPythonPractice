x = [80, 55, 34, 67, 98, 34, 2, 19]
# x = [5,4,3,2,1]


def splitList(l):
    if len(l) > 1:
        left = l[:len(l)//2]
        right = l[len(l)//2:]
        leftSorted = splitList(left)
        rightSorted = splitList(right)
        return mergeList(leftSorted, rightSorted)
    else:
        return l


def mergeList(a, b):
    res = []
    i = 0
    j = 0

    while len(res) < len(a) + len(b):
        if i == len(a):
            res.extend(b[j:])

        elif j == len(b):
            res.extend(a[i:])

        elif a[i] > b[j]:
            res.append(b[j])
            j += 1
        elif a[i] <= b[j]:
            res.append(a[i])
            i += 1
    return res


y = splitList(x)
print(y)
