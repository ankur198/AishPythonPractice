x = [80, 55, 34, 67, 98, 34, 2, 19]
# x = [5,4,3,2,1]

toMerge = []


def splitList(l):
    if len(l) > 1:
        v = l[:len(l)//2]
        w = l[len(l)//2:]
        splitList(v)
        splitList(w)

    else:
        toMerge.append(l)


def merge():
    while len(toMerge) > 1:
        fE = toMerge[0]
        sE = toMerge[1]
        toMerge.pop(0)
        toMerge.pop(0)

        # print(toMerge)
        # print(mergeList(fE,sE))
        toMerge.append(mergeList(fE, sE))


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
        elif a[i]<=b[j]:
            res.append(a[i])
            i += 1
    return res


splitList(x)
# print(toMerge)
merge()
print(toMerge[0])
print(x)
