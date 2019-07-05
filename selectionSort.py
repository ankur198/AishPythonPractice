a = [56, 23, 645, 457, 2346,1, 86, 34]

def getMin(start, end, arr):
    Min = arr[start]
    MinIndex = start
    for i in range(start+1, end):
        if Min > arr[i]:
            Min = arr[i]
            MinIndex = i
    return MinIndex


for Pass in range(len(a)-1):
    MinIndex = getMin(Pass, len(a), a)
    a[MinIndex],a[Pass] = a[Pass],a[MinIndex]
    print('Pass',Pass,':',a)
